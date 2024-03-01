from lib.SpeechUtil import SpeechUtil
from lib.logger import debug

ROLE_USER = "user"
ROLE_ASSISTANT = "assistant"
ROLE_SYSTEM = "system"

class BaseLLM(SpeechUtil):

    roles_mapping = {}

    args = dict(
        api_key = None,
        model   = None
    );

    system_message = None

    message_history = []


    def __init__(self, *args, **kwargs):
        self.roles_mapping[ ROLE_ASSISTANT ] = ROLE_ASSISTANT
        self.roles_mapping[ ROLE_USER ]      = ROLE_USER
        self.roles_mapping[ ROLE_SYSTEM ]    = ROLE_SYSTEM


    # Muunnetaan ohjelman sisäinen rooli mallin rooliksi
    def encodeRole( self, role ):
        return self.roles_mapping[ role ]
    
    # Muunnetaan mallin rooli ohjelman sisäiseksi rooliksi
    def decodeRole( self, role ):
        for key in self.roles_mapping:
            if self.roles_mapping[ key ] == role:
                return key

    def chatToString( self ):
        chat = ""
        for message in self.message_history:
            chat += message.role + ": " + message.content + "\n\n"
        return chat

    def printChat( self ):
        print( self.chatToString() )

    def setSystemMessage( self, message ):
        debug( type(self).__name__, "setSystemMessage", message )

       
        self.system_message = message
        for message in self.message_history:
            if message.role == ROLE_SYSTEM:
                message.content = message
                return;

        self.message_history.append( BaseMessage( content=message, role=ROLE_SYSTEM ))


    def text_to_text_completion(self, messages):
        assert False, "text_to_text_completion not implemented"


    def _text_to_text_completion_fake( self, text ):

        message = BaseMessage( content="Vastaus viestiin: "+text, role=ROLE_ASSISTANT )

        self.message_history.append( message )

        return message.content
    
    

class BaseMessage:
    def __init__(self, *args, **kwargs):
        self.content = kwargs.get("content", "")
        self.role    = kwargs.get("role", "user")
        pass