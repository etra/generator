import datetime

from sqlalchemy import Column, Integer, String, DateTime, func
from aligator.db import db
from aligator.faker import faker
from faker import Faker


class Visit(db.Base):
    __tablename__ = 'visits'
    id = Column(Integer, primary_key=True)
    user_agent = Column(String)
    created_at = Column(DateTime)  # This will set the current timestamp on creation

    @staticmethod
    def create_it(dt: datetime.datetime) -> 'Visit':
    #     #todo: find a better way to make fake users (maybe use name as part of email + make sure cities are consistant)
        return Visit(user_agent=faker.user_agent(), created_at=dt)
