import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    DEBUG = True if os.environ.get("DEBUG", "False") == "True" else False



config = Config()
