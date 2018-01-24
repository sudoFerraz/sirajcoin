import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
import json
import hashlib
import requests

from model import Refer, Subscription

class ostools(object):
    def __init__(self):
        pass

    def db_connection(self):
        engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
        Session = scoped_session(sessionmaker())
        Session.configure(bind=engine)
        session = Session
        return session

class refer_handler(object):
    def __init__(self):
        pass

    def create_refer(self, session, new_key):
        new_refer = model.Refer(pubkey=new_key, count=0)
        session.add(new_refer)
        session.commit()
        session.flush()
        return new_refer

    def update_counter(self, session, key):
        refer = session.query(model.Refer).filter_by(pubkey=key).first()
        refer.count = refer.count + 1
        session.commit()
        session.flush()
        return refer

    def consult_or_create(self, session, key):
        refer = session.query(model.Refer).filter_by(pubkey=key).first()
        if refer:
            refer.count = refer.count + 1
            session.commit()
            session.flush()
            return refer
        else:
            new_refer = model.Refer(pubkey=key, count=1)
            session.add(new_refer)
            session.commit()
            session.flush()
            return new_refer

class subscribe_handler(object):
    def __init__(self):
        pass

    def create_subscription(self, session, key, account):
        new_subscription = model.Subscription(refer_key=key, subscriber_account=account)
        session.add(new_subscription)
        session.commit()
        session.flush()
        return new_subscription

    def auditing(self, session, account):
        found_subscription = session.query(model.Subscription).filter_by(subscriber_account=account).first()
        if found_subscription:
            return True
        else:
            return False
