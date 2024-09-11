#datos para la conexion a la base de datos

dataBaseName="gestordb"
userName ="root"
userPassword=""
connectionPort=3306
server="localhost"


#creando la conexion
dataBaseConection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

print(dataBaseConection)