from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Comunicacion con la base de datos
engine = create_engine('sqlite:///database/tareas.db')

# Crear sesión para realizar transacciones
Session = sessionmaker(bind=engine)
session = Session()

# Mapeo de clases (models.py) para vincular a la base de datos
Base = declarative_base()
