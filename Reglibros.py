# -- Funciones importadas
import Funciones.inicio_sesion as inicio_sesion
import Funciones.validadores as validar


# -- Variables
opciones_menu = ['a', 'b', 'c', 'd', 'e']
personas_reg = {}
libros_reg = {}


# -- Funciones
def registrar_personas():
    global personas_reg
    rut = input('Ingrese el RUT de la persona (12345678-9): ')
    if validar.rut(rut):
        list_rut = personas_reg.keys()
        if rut not in list_rut:
            nombre = input('Ingrese el nombre de la persona: ')
            fecha = validar.fecha(input('Ingrese la fecha de nacimiento: '))
            direccion = input('Ingrese la dirección particular: ')
            telefono = input('Ingrese el número de contacto: ')
            correo = validar.correo(input('Ingrese el correo electronico: '))
            personas_reg.setdefault(str(rut), nombre)
            rut = persona(rut, nombre, fecha, direccion, telefono, correo)
            rut.datos_completos()
            print('Persona registrada con exito')
            print('\n')
        else:
            print('Persona ya se encuentra registrada\n')
    else:
        print('RUT ingresado no es valido\n')
        registrar_personas()
    pass


def registrar_libro():
    global libros_reg
    libros_list = libros_reg.keys()
    isbn = validar.isbn(input('Ingrese el ISBN del libro: '))
    if isbn not in libros_list:
        titulo = input('Ingrese el titulo del libro: ')
        categoria = input('Ingrese la categoría del libro: ')
        fecha_publicacion = validar.fecha(
            input('Ingrese la fecha de publicación (DD/MM/AAAA): '))
        lugar_publicacion = validar.lugar(
            input('Ingrese la procedencia del libro (America/Asia/Europa): '))
        estado = validar.estado(
            input('Ingrese el estado del libro (Nuevo/Usado): '))
        idioma = validar.idioma(
            input('Ingrese el idioma del libro (Ingles/Español/Frances): '))
        autor = input('Ingrese el nombre del autor del libro: ')
        editorial = input('Ingrese la editorial del libro: ')
        cantidad_pag = input(
            'Ingrese la cantidad de paginas que posee el libro: ')
        precio = input('Ingrese el precio del libro: ')
        isbn = libro(isbn, titulo, categoria, fecha_publicacion, lugar_publicacion,
                     estado, idioma, autor, editorial, cantidad_pag, precio)
        libros_reg.setdefault(isbn, titulo)
        isbn.datos_completos()
    else:
        print('El libro ya se encuentra registrado')
    pass


def listar_libros():
    print('\n\nLibros registrados')
    print('\n'.join(libros_reg.values()))
    pass


def buscar_libro():
    print('Buscar libro según su titulo')
    libro_buscado = input('Ingrese el titulo del libro: ')
    for res, libro in libros_reg.items():
        if libro == libro_buscado:
            print('Resultado de busqueda')
            res.datos_completos()
    pass


def abrir_funcion(opc):
    if opc is 'a':
        registrar_personas()
    if opc is 'b':
        registrar_libro()
    if opc is 'c':
        listar_libros()
    if opc is 'd':
        buscar_libro()
    menu_principal()


# -- Menú principal
def menu_principal():
    while True:
        print('-'*20, 'Menú principal', '-'*20,
              '\na. Registrar Personas.',
              '\nb. Registrar Libro.',
              '\nc. Listar Libros Registrados.'
              '\nd. Buscar Libro',
              '\ne. Salir')
        opcion = input('\nOpción: ')
        if opcion in opciones_menu:
            if opcion is 'e':
                print('\n'*100, 'Finalizado')
                break
            abrir_funcion(opcion)
            break
        else:
            print('no existe la opción ingresada')
    pass


def inicio():
    print('Bienvenido')
    if inicio_sesion.validar_user():
        print('\n'*100)
        menu_principal()
    pass


# Proceso principal
if __name__ == "__main__":
    # Clases importadas
    from Clases import libros
    libro = libros.libro
    from Clases import personas as personas
    persona = personas.persona
    inicio()
    pass
