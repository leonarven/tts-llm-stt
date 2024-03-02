OAI="oai"
GTTS="gtts"

FAKE="fake"

def getModel( model ):
    if model == OAI:
        from lib.tts.OpenAITTS import OpenAITTS
        return OpenAITTS()
    
    elif model == GTTS:
        from lib.tts.gTTS import GTTS as GTTSModel
        return GTTSModel()
    
    
    elif model == FAKE:
        from lib.tts.FakeTTS import FakeTTS
        return FakeTTS()

    else:
        raise ValueError(f"Unknown TTS model: { model }")