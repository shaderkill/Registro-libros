import Funciones.validadores as validar
from Clases import libros
libro = libros.libro

# -- Variables
libros_reg = {}

# -- Funciones


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
