from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from loguru import logger as logging


class DB:
    def __init__(self):
        connection_string = os.environ.get('DB_CONNECTION_STRING', 'sqlite:///./data/sqlite/test.db')
        self.engine = create_engine(connection_string)
        logging.info(f"Creating database connection with connection string {connection_string}")
        self.Session = sessionmaker(bind=self.engine)
        self.db_session = self.Session()
        self.Base = declarative_base()

    def add(self, obj):
        self.db_session.add(obj)
        self.db_session.commit()

    def query(self, obj):
        return self.db_session.query(obj)

    def commit(self):
        self.db_session.commit()

    def close(self):
        self.db_session.close()

    def __del__(self):
        self.db_session.close()

db = DB()
