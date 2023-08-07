class Cliente():

    compras = []

    def __init__ (self,usuario,contraseña,email,edad,intereses):
        self.usuario=usuario
        self.contraseña=contraseña
        self.email = email
        self.edad = edad
        self.intereses = intereses

    def __str__ (self):
        return f"El cliente {self.usuario} de {self.edad} años, email: {self.email} con los intereses {self.intereses} ha sido creado"
    
    def comprar(self):
        objeto = input ("Ingrese objeto:")
        precio = input ("Ingrese precio:")
        self.compras.append (
            {"Objeto": objeto, "Precio": precio}
        )

    def imprimir_compras (self):
        if self.compras == []:
            print ("No hay compras")
        else:
            print (f"El cliente {self.usuario} ha comprado:")
            for elemento in self.compras:
                print (elemento)





    