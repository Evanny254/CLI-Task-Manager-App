from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base

engine = create_engine('sqlite:///lib.db')

# Create tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()