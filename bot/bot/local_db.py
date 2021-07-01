from helpers.crackdb import run_bot
from dotenv import load_dotenv
from os import getenv

load_dotenv('envs/.env')

HOST = getenv('DB_HOST')
PORT = getenv('DB_PORT')
USER = getenv('DB_USER')
PSWD = getenv('DB_PASSWORD')
AUTH = getenv('DB_AUTH')
DB = getenv('DB_WORK')
run_bot(HOST, PORT, USER, PSWD, AUTH, DB)