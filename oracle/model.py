import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, Float
from sqlalchemy import ForeignKey, LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Refer(Base):
    __tablename__ = 'Refer'
    id = Column(Integer, primary_key=True)
    pubkey = Column(String)
    count = Column(Integer)

class Subscription(Base):
    __tablename__ = 'Subscription'
    id = Column(Integer, primary_key=True)
    refer_key = Column(String, ForeignKey(Refer.id))
    #For subscribe unsubscribe scenario
    #If youtube supplies a unique accountID for a subscriber
    subscriber_account = Column(String)

engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
