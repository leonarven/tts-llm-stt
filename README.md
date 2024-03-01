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

##

## Run
```
python3.10 main.py
```