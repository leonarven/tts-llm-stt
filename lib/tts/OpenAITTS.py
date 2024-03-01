from time import sleep, time
import openai
from pydub import AudioSegment

from lib.logger import debug
import lib.const as const
from .BaseTTS import BaseTTS

class OpenAITTS(BaseTTS):

    args = dict(
        api_key = None,
        model = None
    )

    def __init__(self, *args, **kwargs):

        # create temporary file and get it's filename
        self.temporary_file = self._initiate_temporary_file()

        self.args["model"] = kwargs.get( "model", "tts-1")

        self.client = openai.OpenAI();
    
    def _initiate_temporary_file( self ):
        return "temp.wav"
    
    def _get_temporary_file( self ):
        return self.temporary_file;


    def text_to_audio( self, text, format="wav" ):
        debug( type(self).__name__, "text_to_audio() :: Muutetaan vastaus puheeksi" )

        if const.DO_FAKE_TTS:
            return self._text_to_audio_fake( text )

        start_time = time()

        response = self.client.audio.speech.create(
            model=self.args["model"],
            voice="nova",
            input=text,
            response_format="opus"
        )


        debug( type(self).__name__, "text_to_audio() :: Valmis! (", time() - start_time, "s)" )

        filename = self._get_temporary_file()

        response.write_to_file( filename )

        return AudioSegment.from_file( filename, codec="opus")

    def _text_to_audio_fake( self, text, **kwargs ):

        sleep(1)

        return super()._text_to_audio_fake( text, **kwargs )


tts = OpenAITTS()