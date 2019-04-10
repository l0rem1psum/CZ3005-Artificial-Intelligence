# CZ3005-Artificial-Intelligence
CZ3005 Artificial Intelligence Lab Assignments

## Description
Lab 4 Talking Box assignment Prolog + Python code.

The talking box is internally programmed with Prolog and Python is used to build a Telegram chatbot as the UI for this talking box.

The Talking Box is called Askid (Ask a Kid's day at school), and can be found [here](t.me/AskidBot) (Note: currently not hosted).

## Prerequisite

* Python 3.6+
* Ubuntu 18.04 LTS (not tested on Windows/MacOS)
* Internet Connection
* Telegram Account
* SWI-Prolog

## Installation

### Step 1: Setup virtual environment
Open Ubuntu 18.04 LTS, make sure Python 3.6+ is installed. Create a virtual environment for the project by typing the following:
```bash
mkdir venv
virtualenv venv
```
Then activate the virtual environment:
```bash
source venv/bin/activate
```

### Step 2: Install SWI-Prolog
Install SWI-Prolog on machine:
```bash
sudo apt install swi-prolog
```
Install Python PySwip module:
```bash
pip install pyswip
```

Test the installation by running the following code in a Python console:
```python
from pyswip import Prolog
prolog = Prolog()
prolog.assertz("cz3005(artificial_intelligence)")
```

### Step 3: Install other Python dependencies
We only need telepot module which can be installed by typing:
```bash
pip install telepot
```

### Step 4: Get a Telegram bot Token
Search 'BotFather' in Telegram and enter the '/newbot' command. Follow the instruction to obtain your 45-digit token.

Go to Askid.py line:83 and replace <YOUR TOKEN> with your token.

### Step 5: Run the bot
```bash
python Askid.py
```
