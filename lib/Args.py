from os import environ
from argparse import ArgumentParser

from lib.logger import debug

from lib.stt.models import getModel as getSTTModel
from lib.llm.models import getModel as getLLMModel
from lib.tts.models import getModel as getTTSModel

from lib.stt.models import SPEECH_RECOGNITION as default_stt
from lib.llm.models import GEMINI_1_0_PRO     as default_llm
from lib.tts.models import OAI                as default_tts

class Args:

    debug = False

    tts = None
    stt = None
    llm = None

    iterations = None

    operator = "SpeechOperator"

    def __init__(self, argv = None):
        if argv:
            import sys
            arg = sys.argv[1:]

        parser = ArgumentParser()

        parser.add_argument( '-a', '--stt', default=default_stt )
        parser.add_argument( '-b', '--llm', default=default_llm )
        parser.add_argument( '-c', '--tts', default=default_tts )
        parser.add_argument( '-d', '--debug', action='store_true' )
        parser.add_argument( '-n', '--iterations', type=int, default=2, help="Used when in debug mode. Number of iterations. When 0, run indefinitely.")
        parser.add_argument( '-o', '--operator', type=str, default="SpeechChamberOperator", help="Used when in debug mode. SpeechOperator or SpeechChamberOperator", choices=["SpeechOperator", "SpeechChamberOperator"])

        args = parser.parse_args()

        self.setDebug( args.debug )
        self.setSTT(   args.stt )
        self.setLLM(   args.llm )
        self.setTTS(   args.tts )
        self.setIterations( args.iterations )
        self.setOperator( args.operator )

        debug( "Args() :: DEBUG:", self.debug )
        debug( "Args() :: STT:",   self.stt   )
        debug( "Args() :: LLM:",   self.llm   )
        debug( "Args() :: TTS:",   self.tts   )
        debug( "Args() :: ITERATIONS:", self.iterations )

    def setDebug( self, debug ):
        self.debug = True if debug else False
        if self.debug:
            environ["DEBUG"] = str( self.debug )
        else:
            environ["DEBUG"] = '' # Clear DEBUG environment variable as '' is False

    def setSTT( self, stt ):

        if not stt:
            raise Exception("STT model not set")

        stt = stt.lower()

        self.stt = getSTTModel( stt )

    def setLLM( self, llm ):
        
        if not llm:
            raise Exception("LLM model not set")

        llm = llm.lower()

        self.llm = getLLMModel( llm )


    def setTTS( self, tts ):
            
        if not tts:
            raise Exception("TTS model not set")

        tts = tts.lower()

        self.tts = getTTSModel( tts )

    def setIterations( self, iterations: int ):
        if iterations > 0:  
            self.iterations = iterations
        else:
            self.iterations = None

    def setOperator( self, operator: str ):
        self.operator = operator

args = Args()