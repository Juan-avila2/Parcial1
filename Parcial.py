#Autor: Juan Felipe Avila

class Libros:
    def __init__(self, autor, id, categoria):
        self.autor = autor
        self.id = id
        self.categoria = categoria  


class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña


def registrar_libro():
    n = int(input("¿Cuántos libros desea registrar?: "))
    for i in range (n):
        autor_libro = input("Ingrese el autor del libro: ")
        id_libro = int(input("Ingrese el código ISBN del libro: "))
        categoria_libro = int(input("De las siguientes, escoja la categoría que considere más adecuada para el libro e ingrese el número en la consola: "  "1.Romance " "2.Aventuras " "3.Filosofía "))
    
        libros = Libros( autor_libro, id_libro, categoria_libro )

def registrar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario a registrar: ")
    contraseña_usuario = input("Ingrese la contraseña del usuario a registrar: ")
    
    usuario = Usuario( nombre_usuario, contraseña_usuario)

def ingreso_usuario():
    usarname = input("Ingrese su nombre de usuario: ")
    password = input("ngrese su contraseña")

    if usarname == nombre_usuario:
        


persona = int(input("¿Usted es un?: 1.Usuario  2.Bbliotecario"))
if persona == 1:

    sacar = int(input("¿Desea "))
else:
    iniciar = int(input("¿Desea registrar un libro?: 1.Si  2.No "))
    if iniciar == 1:
     registrar_libro()
    else:
         pass

    iniciar_registro_usuario = int(input("¿Desea registrar un usuario?: 1.Si 2.No "))
    if iniciar_registro_usuario == 1:
         registrar_usuario()
    else:
        pass

    




