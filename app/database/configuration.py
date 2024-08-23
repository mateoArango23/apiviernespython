# Librerías
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

# Conexión a la base de datos
# nombre Base de Datos
dataBaseName = "gestionbd"
# usuario Base de Datos
userName = "root"
# contraseña del usuario
userPassword = ""
# puerto de conexión
connectionPort = "3306"
# servidor conexión
serverConnection = "localhost"
# creando la conexión
connectionToDataBase = f"mysql + mysqlconnector://{userName}:{userPassword}@{serverConnection}:{connectionPort}/{dataBaseName}"

engine = create_engine (connectionToDataBase)
sessionLocal = sessionmaker(autocomit = False, autoFlush = False, bind = engine) # nosotros le decimos que poner en la BD 