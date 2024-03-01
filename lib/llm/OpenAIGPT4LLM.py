from .OpenAIGPT35LLM import OpenAIGPT35LLM

class OpenAIGPT4LLM(OpenAIGPT35LLM):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args["model"] = kwargs.get("model", "gpt-4")

llm = OpenAIGPT4LLM()