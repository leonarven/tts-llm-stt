import speech_recognition as sr
from time import time
from lib.logger import debug
from lib.stt.BaseSTT import BaseSTT

class FakeSTT( BaseSTT ):

    def audio_to_text( self, filename ):
        debug( type(self).__name__, "audio_to_text()","Kuunnellaan tiedosto")

        return super()._audio_to_text_fake()
    
    def recording_to_text( self, duration=None ):
        debug( type(self).__name__, "recording_to_text()","Kuunnellaan...")

        return super()._recording_to_text_fake()