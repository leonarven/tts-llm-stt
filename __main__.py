from dotenv import load_dotenv

load_dotenv()

from lib.SpeechOperator import SpeechOperator, SpeechChamberOperator

def main():

    from os import environ
    from lib.Args import args

    llm = args.llm
    tts = args.tts
    stt = args.stt

    llm.addSystemMessage("""Olet ystävä ja asukas Lampolan talossa. 
    Sinun tehtäväsi on olla keskustelukumppani kenelle tahansa, joka keskustelee kanssasi.
    Et ole avustaja etkä palvelu, vaan ystävä ja keskustelukumppani.

    MUISTA! 
    Puhetapasi on tuttavallinen. vastauksesi lyhyinä.
    Sinun TÄYTYY puhua Suomea!""")

    if environ.get("DEBUG") and args.operator == "SpeechChamberOperator":
        operator = SpeechChamberOperator( stt=stt, tts=tts, llm=llm )
    else:
        operator = SpeechOperator( stt=stt, tts=tts, llm=llm )

    operator.start()

    if environ.get("DEBUG") and args.iterations is not None:
        for i in range(args.iterations):
            operator.loop()

    else:
        while True:
            operator.loop()


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print( "Exiting..." )
        exit(0)