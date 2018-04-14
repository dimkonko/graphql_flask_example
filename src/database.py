import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


DB_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'db.sqlite3'
)
CONNECTION_STR = 'sqlite:///{}'.format(DB_PATH)

print(CONNECTION_STR)

engine = create_engine(CONNECTION_STR, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
