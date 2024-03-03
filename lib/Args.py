from os import environ
from argparse import ArgumentParser

from lib.logger import debug

from lib.stt.models import getModel as getSTTModel
from lib.llm.models import getModel as getLLMModel
from lib.tts.models import getModel as getTTSModel

from lib.stt.models import SPEECH_RECOGNITION as default_stt
from lib.llm.models import GEMINI_1_0_PRO     as default_llm
from lib.tts.models import OAI                as default_tts

from lib.stt.models import SPEECH_RECOGNITION as default_debug_stt
from lib.llm.models import GROQ_MIXTRAL_8_7B  as default_debug_llm
from lib.tts.models import GTTS               as default_debug_tts

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

        parser.add_argument( '-a', '--stt',        type=str, default='' )
        parser.add_argument( '-b', '--llm',        type=str, default='' )
        parser.add_argument( '-c', '--tts',        type=str, default='' )
        parser.add_argument( '-n', '--iterations', type=int, default=2, help="Used when in debug mode. Number of iterations. When 0, run indefinitely.")
        parser.add_argument( '-o', '--operator',   type=str, default="SpeechChamberOperator", help="Used when in debug mode. SpeechOperator or SpeechChamberOperator", choices=["SpeechOperator", "SpeechChamberOperator"])
        parser.add_argument( '-d', '--debug',      action='store_true' )
        parser.add_argument( '-v', '--verbose',    action='store_true' )

        args = parser.parse_args()

        if args.debug and not args.verbose:
            args.verbose = True

        self.setDebug(      args.debug      )
        self.setVerbose(    args.verbose    )
        self.setSTT(        args.stt        )
        self.setLLM(        args.llm        )
        self.setTTS(        args.tts        )
        self.setIterations( args.iterations )
        self.setOperator(   args.operator   )

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

    def setVerbose( self, verbose ):
        self.verbose = True if verbose else False
        if self.verbose:
            environ["VERBOSE"] = str( self.verbose )
        else:
            environ["VERBOSE"] = ''

    def setSTT( self, stt ):

        if not stt:
            stt = default_debug_stt if self.debug else default_stt

        stt = stt.lower()

        self.stt = getSTTModel( stt )

    def setLLM( self, llm ):
        
        if not llm:
            llm = default_debug_llm if self.debug else default_llm

        llm = llm.lower()

        self.llm = getLLMModel( llm )


    def setTTS( self, tts ):

        if not tts:
            tts = default_debug_tts if self.debug else default_tts

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