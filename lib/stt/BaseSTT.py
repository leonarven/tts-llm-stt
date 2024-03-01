from lib.SpeechUtil import SpeechUtil

fake_texts = [
    "Tuntuu, että tämä viikko on mennyt niin nopeasti!",
    "Aamukahvi on kyllä aina paras hetki päivässä.",
    "Säätiedotus lupasi tänään aurinkoa, mutta näyttääpä taas sateiselta.",
    "Aijai, tämä ruuhka ei näytä hälvenevän hetkeen.",
    "Olipa hyvä leffa eilen illalla, suosittelen!",
    "Kuulostaa hyvältä suunnitelmalta",
    "Tiedätkö, olen miettinyt uuden maton hankkimista olohuoneeseen.",
    "Tiedätkö, joskus kaipaan oikeasti vanhoja kunnon kännykkäaikoja.",
    "Ai niin, täytyy muistaa ostaa maitoa kaupasta palatessa.",
    "Tuntuu, että tämä viikko on mennyt niin nopeasti!"
]

class BaseSTT(SpeechUtil):
    def __init__(self, config=dict()):
        self.config = config

    def audio_to_text( self, filename ):
        assert False, "audio_to_text not implemented"


    def _audio_to_text_fake( self ):
        import random
        return fake_texts[random.randint(0, len(fake_texts)-1)]
    
    def _recording_to_text_fake( self ):
        return self._audio_to_text_fake()