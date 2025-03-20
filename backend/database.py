from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:///project.db')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import model
    Base.metadata.create_all(bind=engine)
    db_session.remove()