# -- Funciones importadas
from Funciones import inicio_sesion, reglibros, regpersonas

# -- Variables del menú
opciones_menu = ['a', 'b', 'c', 'd', 'e']


# -- Funciones
def abrir_funcion(opc):
    if opc is 'a':
        regpersonas.registrar_personas()
    if opc is 'b':
        reglibros.registrar_libro()
    if opc is 'c':
        reglibros.listar_libros()
    if opc is 'd':
        reglibros.buscar_libro()
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
                print('\n'*50, 'Finalizado')
                break
            abrir_funcion(opcion)
            break
        else:
            print('no existe la opción ingresada')
    pass


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
