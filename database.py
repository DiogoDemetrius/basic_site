from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Substitua os valores abaixo pelos dados do seu servidor MySQL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:senha@localhost/prog_web"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
