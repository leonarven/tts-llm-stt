GROQ_MIXTRAL_8_7B    = "mixtral-8x7b-32768"
GROQ_LLAMA2_70B      = "llama2-70b-4096"

MISTRAL_LARGE_LATEST = "mistral-large-latest"

GEMINI_1_0_PRO       = "gemini-1.0-pro"

GPT_3_5              = "gpt-3.5-turbo"
GPT_4_0              = "gpt-4.0-turbo"

FAKE                 = "fake"

def getModel( model ):
    if model == GROQ_MIXTRAL_8_7B:
        from lib.llm.GroqLLM import GroqLLM
        return GroqLLM( model=model )

    elif model == GROQ_LLAMA2_70B:
        from lib.llm.GroqLLM import GroqLLM
        return GroqLLM( model=model )

    elif model == MISTRAL_LARGE_LATEST:
        from lib.llm.MistralLLM import MistralLLM
        return MistralLLM( model=model )

    elif model == GEMINI_1_0_PRO:
        from lib.llm.GeminiLLM import GeminiLLM
        return GeminiLLM( model=model )

    elif model == GPT_3_5:
        from lib.llm.OpenAIGPT35LLM import OpenAIGPT35LLM
        return OpenAIGPT35LLM( model=model )

    elif model == GPT_4_0:
        from lib.llm.OpenAIGPT4LLM import OpenAIGPT4LLM
        return OpenAIGPT4LLM( model=model )


    elif model == FAKE:
        from lib.llm.FakeLLM import FakeLLM
        return FakeLLM( model=model )

    else:
        raise ValueError(f"Unknown LLM model: { model }")