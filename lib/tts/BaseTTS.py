from lib.SpeechUtil import SpeechUtil

class BaseTTS(SpeechUtil):
    def __init__( self, config=dict() ):
        self.config = config

    def text_to_audio( self, text ):
        assert False, "text_to_audio not implemented"

    def _text_to_audio_fake( self, text, **kwargs ):
        from pydub.generators import Sine

        #generate sine sound via using pydub
        return Sine(440).to_audio_segment(duration=1000)

        #assert False, "text_to_fake_audio not implemented"