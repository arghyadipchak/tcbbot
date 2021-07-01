from tcbbot import run_bot
from dotenv import load_dotenv
from os import getenv

load_dotenv('envs/.env')
run_bot(getenv('BOT_TOKEN'))