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
vim .env lib/const.py
```

## Run
```
python3.10 main.py
```
And speak.

## Usage

**Parameters**
- `-d` / `--debug` - Debug mode
- `-a` / `--stt` - Speech to text -model
- `-b` / `--llm` - LLM-model
- `-c` / `--tts` - Text to speech -model
- `-n` / `--iterations` - Count of iterations when in debug mode
- `-o` / `--operator` - The used operator for handling the loop when in debug mode. *"SpeechOperator"* or *"SpeechCommandOperator"*