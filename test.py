from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
from aligator.fakers.datasets import Cities, Countries, Products
Base = declarative_base()
fake = Faker()

fake.add_provider(Cities)
fake.add_provider(Countries)
fake.add_provider(Products)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    country = Column(String)
    email = Column(String)

    @staticmethod
    def create_user() -> 'User':
        #todo: find a better way to make fake users (maybe use name as part of email + make sure cities are consistant)
        return User(name=fake.name(), email=fake.email())

# Setting up the database connection and session
# connection string
engine = create_engine('sqlite:///./data/sqlite/test.db')

#create session
Session = sessionmaker(bind=engine)

# create tables
Base.metadata.create_all(engine)

# create session
db_session = Session()

# for _ in range(10):
db_session.add(User.create_user())
db_session.commit()

exit()




#
#
# print(f"{fake.name()} lives in {fake.address()}")
