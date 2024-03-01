from dotenv import load_dotenv

load_dotenv()

import sys

sys.path.append('.')

import lib.const as const

from lib.SpeechOperator import SpeechOperator, SpeechChamberOperator

from lib.stt.SpeechRecognitionSTT import stt
from lib.llm.GeminiLLM import llm

if const.DEBUG:
    from lib.tts.gTTS import tts
    #from lib.llm.OpenAIGPT35LLM import llm
    #from lib.llm.MistralLLM import llm
else:
    from lib.tts.OpenAITTS import tts
    #from lib.llm.OpenAIGPT4LLM import llm

llm.setSystemMessage("""Olet ystävä ja asukas Lampolan talossa. 
Sinun tehtäväsi on olla keskustelukumppani kenelle tahansa, joka keskustelee kanssasi.
Et ole avustaja etkä palvelu, vaan ystävä ja keskustelukumppani.

MUISTA! 
Puhetapasi on tuttavallinen. vastauksesi lyhyinä.
Sinun TÄYTYY puhua Suomea!""")

if const.DEBUG:
    operator = SpeechChamberOperator( stt=stt, tts=tts, llm=llm )
else:
    operator = SpeechOperator( stt=stt, tts=tts, llm=llm )

operator.start()

def main(args):

    if const.DEBUG:
        for i in range(2):
            operator.loop()

    else:
        while True:
            operator.loop()


if __name__ == '__main__':
    main(sys.argv[1:])