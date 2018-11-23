# coding: utf-8
from sqlalchemy import Column, Date, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Booking(Base):
    __tablename__ = 'booking'

    id = Column(SMALLINT(5), primary_key=True)
    user_id = Column(SMALLINT(5), nullable=False)
    book_id = Column(SMALLINT(5), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class User(Base):
    __tablename__ = 'user'

    id = Column(SMALLINT(5), primary_key=True)
    first_name = Column(String(64), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
