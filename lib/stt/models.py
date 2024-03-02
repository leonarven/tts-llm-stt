SPEECH_RECOGNITION = "speechrecognition"

FAKE = "fake"

def getModel( model: str ):
    if model == SPEECH_RECOGNITION:
        from lib.stt.SpeechRecognitionSTT import SpeechRecognitionSTT
        return SpeechRecognitionSTT()


    elif model == FAKE:
        from lib.stt.FakeSTT import FakeSTT
        return FakeSTT()

    else:
        raise ValueError(f"Unknown STT model: { model }")