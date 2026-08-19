# إعدادات النموذج اللغوي في TITAN

MODEL_NAME = "TITAN-1B"

MODEL_PARAMETERS = 1_000_000_000

MODEL_DOMAIN = "code"

MODEL_TYPE = "causal_language_model"

QUANTIZATION = "not_set"

CONTEXT_LENGTH = 2048

MAX_NEW_TOKENS = 512


def get_model_config():
    return {
        "name": MODEL_NAME,
        "parameters": MODEL_PARAMETERS,
        "domain": MODEL_DOMAIN,
        "type": MODEL_TYPE,
        "quantization": QUANTIZATION,
        "context_length": CONTEXT_LENGTH,
        "max_new_tokens": MAX_NEW_TOKENS
    }
