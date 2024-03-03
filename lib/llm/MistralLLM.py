from requests import post
from os import getenv
from time import sleep

from lib.logger import debug
import lib.llm.models as models

from .OpenAIGPT35LLM import OpenAIGPT35LLM
from lib.llm.BaseLLM import BaseMessage, ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT

class MistralLLM(OpenAIGPT35LLM):

    api_endpoint = "https://api.mistral.ai/v1/chat/completions";

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args["api_key"] = kwargs.get("api_key", getenv("MISTRAL_API_KEY"))
        self.args["model"] = kwargs.get("model", models.MISTRAL_LARGE_LATEST )

    def _chat_completion_single_message( self, text ) -> BaseMessage:
        return self._chat_completion_messages( self._text_to_messages( text ))
    
    def _chat_completion_messages( self, messages ) -> BaseMessage:

        json = {
            "model": f"{ self.args['model'] }",
            "messages": messages
        }

        if self.max_tokens:
            json["max_tokens"] = self.max_tokens

        response = post(
            self.api_endpoint,
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer { self.args['api_key'] }"
            },
            json = json
        )

        completion = response.json()

        role = completion["choices"][0]["message"]["role"]
        content = completion["choices"][0]["message"]["content"]
        
        return BaseMessage( content=content, role=role )
