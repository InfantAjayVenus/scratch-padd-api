from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Sequence

Base = declarative_base()

class Pad(Base):
    __tablename__ = 'pad'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)

try:
    engine = create_engine("sqlite:///dev.db")
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

except Exception:
    print('>>>>>>>>Error Initializing DB<<<<<<<<<<<')
    print(Exception)
