from lib.logger import debug
from lib.tts.BaseTTS import BaseTTS

class FakeTTS( BaseTTS ):
    
    def text_to_audio( self, text, lang="fi" ):
        debug( type(self).__name__, "text_to_audio() :: Muutetaan vastaus puheeksi" )
        return self._text_to_audio_fake( text )