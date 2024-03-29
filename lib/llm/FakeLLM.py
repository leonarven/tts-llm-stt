from time import sleep
from lib.logger import debug
from lib.llm.BaseLLM import BaseLLM, BaseMessage, ROLE_USER, ROLE_ASSISTANT

class FakeLLM(BaseLLM):
    
    def text_to_text_completion( self, text ):
        debug( type(self).__name__, "text_to_text_completion() :: Luodaan vastaus" )
        
        return self._text_to_text_completion_fake( text )
    

    def _text_to_text_completion_fake( self, text ):

        self._text_to_messages( text )

        sleep(1)

        return super()._text_to_text_completion_fake( text )

    def _chat_completion_messages( self, messages: list ) -> BaseMessage:

        text = messages[ len(messages)-1 ]["content"]

        return BaseMessage( content="Vastaus viestiin: "+text, role=ROLE_ASSISTANT )



    def _text_to_messages( self, text ):

        self.message_history.append( BaseMessage( content=text, role=ROLE_USER ))

        messages = []
        for message in self.message_history:
            messages.append( { "role": message.role, "content": message.content } )

        return messages