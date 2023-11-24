from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.employe import CustomUser
from models.role import Role
from models.client import Client
from models.contract import Contract
from models.event import Event
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

database_user = os.environ.get("DATABASE_USER")
database_password = os.environ.get("DATABASE_PASSWORD")
database_host = os.environ.get("DATABASE_HOST")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

db_url = f"mysql+mysqldb://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}"
# db_url = f"mysql+mysqlconnector://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}"

engine = create_engine(db_url)

try:
    conn = engine.connect()
    # Role.metadata.drop_all(bind=conn)
    Role.metadata.create_all(bind=conn)
    # CustomUser.metadata.drop_all(bind=conn)
    CustomUser.metadata.create_all(bind=conn)
    Client.metadata.create_all(bind=conn)
    Contract.metadata.create_all(bind=conn)
    Event.metadata.create_all(bind=conn)

except Exception as ex:
    print(ex)

Session = sessionmaker(bind=engine)
Session = Session()
