from pydub.playback import play

from lib.llm.BaseLLM import ROLE_USER

class SpeechOperator:

    iteration = 0

    running = False

    stt = None;
    tts = None;
    llm = None;

    def __init__(self, **kwargs):

        self.stt = kwargs.get( "stt", None )
        self.tts = kwargs.get( "tts", None )
        self.llm = kwargs.get( "llm", None )

        assert self.stt is not None, "SpeechOperator::__init__() :: Puuttuu puheentunnistaja"
        assert self.tts is not None, "SpeechOperator::__init__() :: Puuttuu puheentuottaja"
        assert self.llm is not None, "SpeechOperator::__init__() :: Puuttuu kielimalli"

        self.stt.registerOperator( self )
        self.tts.registerOperator( self )
        self.llm.registerOperator( self )
        
        pass

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def loop(self):
        if self.running:
            self.iteration += 1
            print( "=========================" )
            self.run()

    def run(self):

        text = self.fetchMessage()

        if text == "": return

        #play( self.tts.text_to_audio( text ))

        response = self.fetchResponse( text )

        self.printChat();

        self.playbackText( response )

    def fetchMessage( self ):
        text = self.stt.recording_to_text()
        text = text.strip();

        if text == "":
            print( "INFO :: Ei kuultu mitään" )
        else:
            print( "INFO :: Sinä sanoit:", text )

        return text;

    def fetchResponse( self, text ):
        return self.llm.text_to_text_completion( text )

    def playbackText(self, response):
        play( self.tts.text_to_audio( response ))

    def printChat(self):
        print( "\nINFO :: Käyty keskustelu:")
        self.llm.printChat()

class SpeechChamberOperator( SpeechOperator ):

    def fetchMessage( self ):

        if self.iteration > 1:
            last_message = self.llm.message_history[ len(self.llm.message_history)-1 ]

            messages = [{ "role": self.llm.encodeRole( ROLE_USER ), "content": last_message.content }]

            result = self.llm._chat_completion_messages( messages )

            content = result.content

        else:
            content = self.stt._recording_to_text_fake();

        print( self.llm.chatToString() + "user: " + content + "\n\n" )

        self.playbackText( content )

        return content