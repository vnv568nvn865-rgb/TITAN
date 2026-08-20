#include <jni.h>
#include <string>
#include <vector>

#include "llama.h"

extern "C"
JNIEXPORT jlong JNICALL
Java_com_titan_llama_LlamaBridge_loadModel(
        JNIEnv* env,
        jobject,
        jstring modelPath) {

    const char* path =
            env->GetStringUTFChars(modelPath, nullptr);

    llama_model_params model_params =
            llama_model_default_params();

    llama_model* model =
            llama_model_load_from_file(
                    path,
                    model_params
            );

    env->ReleaseStringUTFChars(modelPath, path);

    return reinterpret_cast<jlong>(model);
}

extern "C"
JNIEXPORT void JNICALL
Java_com_titan_llama_LlamaBridge_freeModel(
        JNIEnv*,
        jobject,
        jlong modelHandle) {

    llama_model* model =
            reinterpret_cast<llama_model*>(modelHandle);

    if (model != nullptr) {
        llama_model_free(model);
    }
}

extern "C"
JNIEXPORT jstring JNICALL
Java_com_titan_llama_LlamaBridge_generate(
        JNIEnv* env,
        jobject,
        jlong modelHandle,
        jstring promptText) {

    llama_model* model =
            reinterpret_cast<llama_model*>(modelHandle);

    if (model == nullptr) {
        return env->NewStringUTF(
                "ERROR: model is not loaded"
        );
    }

    const char* promptChars =
            env->GetStringUTFChars(promptText, nullptr);

    std::string prompt(promptChars);

    env->ReleaseStringUTFChars(
            promptText,
            promptChars
    );

    llama_context_params ctx_params =
            llama_context_default_params();

    ctx_params.n_ctx = 2048;
    ctx_params.n_batch = 512;
    ctx_params.n_ubatch = 512;

    llama_context* ctx =
            llama_init_from_model(
                    model,
                    ctx_params
            );

    if (ctx == nullptr) {
        return env->NewStringUTF(
                "ERROR: failed to create context"
        );
    }

    llama_set_n_threads(
            ctx,
            4,
            4
    );

    const llama_vocab* vocab =
            llama_model_get_vocab(model);

    int32_t tokenCount =
            -llama_tokenize(
                    vocab,
                    prompt.c_str(),
                    prompt.size(),
                    nullptr,
                    0,
                    true,
                    true
            );

    if (tokenCount <= 0) {
        llama_free(ctx);

        return env->NewStringUTF(
                "ERROR: failed to tokenize prompt"
        );
    }

    std::vector<llama_token> tokens(
            tokenCount
    );

    if (llama_tokenize(
            vocab,
            prompt.c_str(),
            prompt.size(),
            tokens.data(),
            tokens.size(),
            true,
            true
    ) < 0) {

        llama_free(ctx);

        return env->NewStringUTF(
                "ERROR: tokenization failed"
        );
    }

    llama_batch batch =
            llama_batch_get_one(
                    tokens.data(),
                    tokens.size()
            );

    if (llama_decode(ctx, batch) != 0) {
        llama_free(ctx);

        return env->NewStringUTF(
                "ERROR: prompt decoding failed"
        );
    }

    llama_sampler_chain_params samplerParams =
            llama_sampler_chain_default_params();

    llama_sampler* sampler =
            llama_sampler_chain_init(
                    samplerParams
            );

    if (sampler == nullptr) {
        llama_free(ctx);

        return env->NewStringUTF(
                "ERROR: failed to create sampler"
        );
    }

    llama_sampler_chain_add(
            sampler,
            llama_sampler_init_temp(0.7f)
    );

    llama_sampler_chain_add(
            sampler,
            llama_sampler_init_top_p(0.9f, 1)
    );

    llama_sampler_chain_add(
            sampler,
            llama_sampler_init_greedy()
    );

    std::string output;

    const int maxTokens = 128;

    for (int i = 0; i < maxTokens; ++i) {

        llama_token newToken =
                llama_sampler_sample(
                        sampler,
                        ctx,
                        -1
                );

        if (llama_vocab_is_eog(
                vocab,
                newToken
        )) {
            break;
        }

        char piece[512];

        int pieceSize =
                llama_token_to_piece(
                        vocab,
                        newToken,
                        piece,
                        sizeof(piece),
                        0,
                        true
                );

        if (pieceSize < 0) {
            break;
        }

        output.append(
                piece,
                pieceSize
        );

        batch =
                llama_batch_get_one(
                        &newToken,
                        1
                );

        if (llama_decode(
                ctx,
                batch
        ) != 0) {
            break;
        }
    }

    llama_sampler_free(sampler);
    llama_free(ctx);

    return env->NewStringUTF(
            output.c_str()
    );
}
