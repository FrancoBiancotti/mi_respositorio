from cliente import Cliente

#Fórmula de registro

def Registro (BDD):
    while True:
        usuario = input ("Ingrese su usuario2:")
        if usuario in BDD:
            print ("El usuario ya existe")
        else:
            break
    contraseña = input ("Ingrese su contraseña:")
    BDD [usuario] = contraseña
    email = input ("Ingrese su email:")
    edad = input ("Ingrese su edad:")
    intereses = input ("Ingrese sus intereses:")
    return Cliente (usuario,contraseña,email,edad,intereses)

#Leer data

def leerdata (BDD):
    print (f"La info almacenada en la base de datos es: {BDD}")

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