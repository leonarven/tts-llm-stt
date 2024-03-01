
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from lib.logger import debug
import lib.const as const
from lib.tts.BaseTTS import BaseTTS

class GTTS( BaseTTS ):
    
    def text_to_audio( self, text, lang="fi" ):
        debug( type(self).__name__, "text_to_audio() :: Muutetaan vastaus puheeksi" )

        if const.DO_FAKE_TTS:
            return self._text_to_audio_fake( text )

        buf = self.text_to_audio_bytesio( text, lang )

        sound = AudioSegment.from_file( buf, "mp3" )

        sound = sound.speedup(playback_speed=1.5)

        return sound;

    def text_to_audio_bytesio( self, text, lang="fi" ):

        tts = self._text_to_tts( text, lang )

        buf = BytesIO()
        
        tts.write_to_fp( buf )
        
        buf.seek( 0 )

        return buf;

    def text_to_audio_file( self, text, filename, lang="fi" ):

        tts = self._text_to_tts( text, lang )

        tts.save( filename )

    def _text_to_tts( self, text, lang="fi" ):
        return gTTS( text, lang=lang )



tts = GTTS()