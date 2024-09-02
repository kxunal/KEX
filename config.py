from os import getenv
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")
  

#Necessary Variables 
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
LOG_ID = int(getenv("LOG_ID"))
SUDOERS = list(map(int, getenv("SUDOERS", "").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
