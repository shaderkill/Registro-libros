# -- Encode: UTF-8
# -- Python version: 3.7.3 64 Bits

# -- Funciones importadas
from Funciones import inicio_sesion
from Funciones import reglibros
from Funciones import regpersonas


# -- Variables del menú
opciones_menu = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# -- Funciones relacionadas al menú
# -- Selección de opción
def abrir_funcion(opc):
    if opc is 'a':
        regpersonas.registrar_personas()
    if opc is 'b':
        reglibros.registrar_libro()
    if opc is 'c':
        reglibros.listar_libros()
    if opc is 'd':
        reglibros.buscar_libro()
    if opc is 'e':
        reglibros.eliminar_libro()
    if opc is 'f':
        regpersonas.listar_personas()
    menu_principal()


# -- Menú principal
def menu_principal():
    while True:
        print('\n'*50)
        print('-'*20, 'Menú principal', '-'*20,
              '\na. Registrar Personas.',
              '\nb. Registrar Libro.',
              '\nc. Listar Libros Registrados.'
              '\nd. Buscar Libro.',
              '\ne. Eliminar Libro.',
              '\nf. Listar personas.'
              '\ng. Salir.')
        opcion = input('\nOpción: ')
        if opcion in opciones_menu:
            if opcion is 'g':
                print('\n'*50, 'Finalizado')
                break
            abrir_funcion(opcion)
            break
        else:
            print('no existe la opción ingresada')
    pass

# -- Inicio de la aplicación


def inicio():
    print('Bienvenido')
    if inicio_sesion.validar_user():
        print('\n'*50)
        menu_principal()
    pass


# Proceso principal
if __name__ == "__main__":
    inicio()
    pass
