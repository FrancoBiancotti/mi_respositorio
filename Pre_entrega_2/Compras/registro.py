from cliente import Cliente

#Fórmula de registro

def Registro ():
    usuario = input ("Ingrese su usuario:")
    contraseña = input ("Ingrese su contraseña:")
    email = input ("Ingrese su email:")
    edad = input ("Ingrese su edad:")
    intereses = input ("Ingrese sus intereses:")
    return Cliente (usuario,contraseña,email,edad,intereses)