#include <jni.h>
#include <string>
#include "llama.h"

extern "C"
JNIEXPORT jlong JNICALL
Java_com_titan_llama_LlamaBridge_loadModel(
        JNIEnv* env,
        jobject,
        jstring modelPath) {

    const char* path = env->GetStringUTFChars(modelPath, nullptr);

    llama_model_params model_params = llama_model_default_params();

    llama_model* model = llama_model_load_from_file(
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

    auto* model =
        reinterpret_cast<llama_model*>(modelHandle);

    if (model != nullptr) {
        llama_model_free(model);
    }
}
