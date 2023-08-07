#Definición de diccionario
BD = {}
#Fórmula de registro
def registro (BDD):
    while True:
        usuario = input ("Ingrese su usuario:")
        if usuario in BDD:
            print ("El usuario ya existe")
        else:
            break
    contraseña = input ("Ingrese su contraseña:")
    BD [usuario] = contraseña
registro (BD)
#Leer data
def leerdata (BDD):
    print (f"La info almacenada en la base de datos es: {BD}")
leerdata(BD)
#Login
def login (BDD):
    while True:
        usuario = input ("Ingrese su usuario:")
        if usuario in BDD:
            break
        print ("El usuario no existe")
    while True:
        contraseña = input ("Ingrese su contraseña:")
        if BDD [usuario] == contraseña:
            break
        print ("La contraseña es incorrecta")
    print ("Has iniciado sesión correctamente")
login (BD)