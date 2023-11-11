from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.employe import CustomUser
from models.role import Role

database_user = "root"
database_password = "LOGviZOvpn2004"
database_host = "localhost"
database_port = "3306"
database_name = "epicevents"

db_url = f"mysql+mysqlconnector://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}"

engine = create_engine(db_url)

try:

    conn = engine.connect()
    print("success")
    # Role.metadata.drop_all(bind=conn)
    Role.metadata.create_all(bind=conn)
    # CustomUser.metadata.drop_all(bind=conn)
    CustomUser.metadata.create_all(bind=conn)

except Exception as ex:
    print(ex)

Session = sessionmaker(bind=engine)
Session = Session()
