I wanted an AI to live inside of old telephone, so I created this.

## Setup
1. run
```
python3.10 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
2. configurate
```
cp dotenv.example.txt .env
```

## Run
```
python3.10 .
```
And speak.

Or to run without reading microphone when testing (audio output is still enabled)
```
python3.10 . --debug
```

Or even more quick to run without microphone and output audio
```
python3.10 . --debug --tts=fake
```

## Usage

**Parameters**
- `-d` / `--debug` - Debug mode
- `-a` / `--stt` - Speech to text -model
- `-b` / `--llm` - LLM-model
- `-c` / `--tts` - Text to speech -model
- `-n` / `--iterations` - Count of iterations when in debug mode
- `-o` / `--operator` - The used operator for handling the loop when in debug mode. *"SpeechOperator"* or *"SpeechCommandOperator"*

Current defaults available in Args.py. Currently:

#### Normal mode
- stt = `SpeechRecognition`
- llm = `gemini-1.0-pro`
- tts = OpenAI TTS as `oai`

#### Debug mode
- stt = `SpeechRecognition`
- llm = `groq-mixtral-8.7b`
- tts = `gTTS`
