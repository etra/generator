import datetime

from sqlalchemy import Column, Integer, String, DateTime, func
from aligator.db import db
from aligator.faker import faker
from faker import Faker


class UserType:
    NEW_USER = 'new_user'
    RETURNING_USER = 'returning_user'
    REGISTERED_USER = 'registered_user'



class Visit(db.Base):
    __tablename__ = 'visits'
    id = Column(Integer, primary_key=True)
    user_agent = Column(String)
    user_type = Column(String)
    created_at = Column(DateTime)  # This will set the current timestamp on creation

    @staticmethod
    def create_it(dt: datetime.datetime, user_type) -> 'Visit':
    #     #todo: find a better way to make fake users (maybe use name as part of email + make sure cities are consistant)
        return Visit(
            user_type=user_type,
            user_agent=faker.user_agent(),
            created_at=dt
        )


class Search(db.Base):
    __tablename__ = 'searches'
    id = Column(Integer, primary_key=True)
    visit_id = Column(Integer)
    created_at = Column(DateTime)  # This will set the current timestamp on creation

    @staticmethod
    def create_it(dt: datetime.datetime, visit_id) -> 'Visit':
        #     #todo: find a better way to make fake users (maybe use name as part of email + make sure cities are consistant)
        return Search(
            visit_id=visit_id,
            created_at=dt
        )


class Order(db.Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    search_id = Column(Integer)
    created_at = Column(DateTime)  # This will set the current timestamp on creation

    @staticmethod
    def create_it(dt: datetime.datetime, search_id) -> 'Visit':
        #     #todo: find a better way to make fake users (maybe use name as part of email + make sure cities are consistant)
        return Order(
            search_id=search_id,
            created_at=dt
        )
