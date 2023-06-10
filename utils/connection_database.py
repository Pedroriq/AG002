import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

user = (os.environ['USER'])
password = (os.environ['PASSWORD'])
host = (os.environ['HOST'])
port = (os.environ['PORT'])


def connect():
    engine = create_engine(f'mysql://{user}:{password}@{host}:{port}/ag002')
    con = engine.connect()
    return con
