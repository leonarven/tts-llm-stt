from requests import post
from os import getenv
from time import sleep

import lib.const as const
from lib.logger import debug

from .OpenAIGPT35LLM import OpenAIGPT35LLM
from lib.llm.BaseLLM import BaseMessage, ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT

class MistralLLM(OpenAIGPT35LLM):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args["api_key"] = kwargs.get("api_key", getenv("MISTRAL_API_KEY"))
        self.args["model"] = kwargs.get("model", "mistral-large-latest")

    def _chat_completion_single_message( self, text ) -> BaseMessage:
    
        response = post(
            "https://api.mistral.ai/v1/chat/completions",
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer { self.args['api_key'] }"
            },
            json = {
                "model": f"{ self.args['model'] }",
                "messages": self._text_to_messages( text )
            }
        )

        completion = response.json()

        role = completion["choices"][0]["message"]["role"]
        content = completion["choices"][0]["message"]["content"]
        
        return BaseMessage( content=content, role=role )

llm = MistralLLM()