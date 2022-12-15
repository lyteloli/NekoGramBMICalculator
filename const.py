from NekoGram.storages.mysql import MySQLStorage
from dotenv import load_dotenv
from NekoGram import Neko
import os

load_dotenv()

MYSQL_USER: str = os.getenv('MYSQL_USER')
MYSQL_PASSWORD: str = os.getenv('MYSQL_PASSWORD')
MYSQL_DB: str = os.getenv('MYSQL_DB')


STORAGE: MySQLStorage = MySQLStorage(database=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASSWORD, default_language='ru')
NEKO: Neko = Neko(token=os.getenv('BOT_TOKEN'), storage=STORAGE)
