import speech_recognition as sr

from lib.logger import debug
import lib.const as const 
from lib.stt.BaseSTT import BaseSTT

class SpeechRecognitionSTT( BaseSTT ):

    def audio_to_text( self, filename ):
        debug( type(self).__name__, "audio_to_text()","Kuunnellaan tiedosto")

        if const.DO_FAKE_SST:
            return super()._audio_to_text_fake()

        with sr.AudioFile( filename ) as source:
            return self._audio_source_to_text( source )
    
    def recording_to_text( self, duration=None ):
        debug( type(self).__name__, "recording_to_text()","Kuunnellaan...")

        if const.DO_FAKE_SST:
            return super()._recording_to_text_fake()
        
        r = sr.Recognizer()

        with sr.Microphone() as source:

            if duration is None:
                debug( type(self).__name__, "recording_to_text()","Kuunnellaan taustaa...")
                r.adjust_for_ambient_noise( source )

            return self._audio_source_to_text( source, duration=duration, recognizer=r )

    def _audio_source_to_text( self, source, **kwargs ):
        debug( type(self).__name__, "recording_to_text()","Kuunnellaan...")

        r = kwargs.get("recognizer", sr.Recognizer())

        # has kwarg duration
        if "duration" in kwargs and kwargs["duration"] is not None:
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=kwargs["duration"])
        else:
            audio_data = r.listen(source)

        try:
            text = self._recognize( r, audio_data )
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""
        except Exception as e:
            print("Error: {0}".format(e))
            return ""

        return text

    def _recognize( self, recognizer, audio_data, language='fi' ):
        debug( type(self).__name__, "_recognize()","Tunnistetaan...")
        start_time = time()
        response = recognizer.recognize_google( audio_data, language=language )
        debug( type(self).__name__, "_recognize() :: Valmis! (", time() - start_time, "s)" )
        return response


stt = SpeechRecognitionSTT()