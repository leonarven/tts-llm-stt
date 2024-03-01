from requests import post
from os import getenv
from time import sleep

import lib.const as const
from lib.logger import debug

from .OpenAIGPT35LLM import OpenAIGPT35LLM
from lib.llm.BaseLLM import BaseMessage, ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT

class GroqLLM(OpenAIGPT35LLM):

    api_endpoint = "https://api.groq.com/openai/v1/chat/completions"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args["api_key"] = kwargs.get("api_key", getenv("GROQ_API_KEY"))
        self.args["model"] = kwargs.get("model", "mixtral-8x7b-32768")



    def _chat_completion_messages( self, messages ) -> BaseMessage:
    
        completion = self._run_chat_completion( messages )

        role = completion["choices"][0]["message"]["role"]
        content = completion["choices"][0]["message"]["content"]
        
        return BaseMessage( content=content, role=role )
    
    def _run_chat_completion( self, messages ):

        response = post(
            self.api_endpoint,
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer { self.args['api_key'] }"
            },
            json = {
                "model": f"{ self.args['model'] }",
                "messages": messages
            }
        )

        completion = response.json()

        print(completion)
        return completion

llm = GroqLLM()