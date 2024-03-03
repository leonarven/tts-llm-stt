from lib.logger import debug
from lib.tts.BaseTTS import BaseTTS

from pydub import AudioSegment
from pydub.playback import play

assets_path = "assets/audio/niin/"
assets = [
    ( "niin", "niin.opus", {"codec":"opus"} ),
    ( "mm",   "mm.opus",   {"codec":"opus"} )
]

sounds = {};

class StaticPrerecordingsTTS( BaseTTS ):
    
    def text_to_audio( self, text, lang="fi" ):
        debug( type(self).__name__, "text_to_audio() :: Muutetaan vastaus puheeksi" )
        
        text = text.lower()

        string, filename, opts = self.resolveAsset( text )

        filepath = assets_path + filename

        if string != text:
            debug( type(self).__name__, f"text_to_audio() :: Valittiin vastaus '{ string }' tekstin '{ text }' sijaan.")

        self.playSound( filepath, opts )

    def resolveAsset( self, text ):

        string   = text
        filename = None
        opts     = None

        distance = 9999

        for asset in assets:

            _string, _filename, _opts = asset
            if _string == text:
                distance = 0
                string   = _string
                filename = _filename
                opts     = _opts
                break;
            else:
                _distance = self.levenshtein_distance( _string, text )

                if _distance < distance:
                    string   = _string
                    distance = _distance
                    filename = _filename
                    opts     = _opts
        
        return string, filename, opts

    def playSound( self, filepath, opts:dict ):
        debug( type(self).__name__, "playSound()", filepath )

        if filepath not in sounds:
            sounds[ filepath ] = AudioSegment.from_file( filepath, codec=opts.get("codec", "wav") )

        play( sounds[ filepath ] )

    def levenshtein_distance( self, a, b ):
        if not a: return len(b)
        if not b: return len(a)
        return min(self.levenshtein_distance(a[1:], b[1:])+(a[0] != b[0]), self.levenshtein_distance(a[1:], b)+1, self.levenshtein_distance(a, b[1:])+1)