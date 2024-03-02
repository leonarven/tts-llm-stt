from .OpenAIGPT35LLM import OpenAIGPT35LLM
import lib.llm.models as models

class OpenAIGPT4LLM(OpenAIGPT35LLM):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args["model"] = kwargs.get("model", models.GPT_4_0)