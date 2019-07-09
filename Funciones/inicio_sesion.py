# Datos usuarios
useradmin = {'admin': 'adminuser'}

# -- Validación de usuario y contraseña


def validar_user():
    global useradmin
    for i in range(3):
        list_keys = useradmin.keys()
        user = input('Ingrese el nombre de usuario: ')
        if user in list_keys:
            return validar_pass(user)
        else:
            print('Error: usuario no existe',
                  '\ningrese un usuario valido (intento %d de 3)\n\n' % (i+1))
        pass


def validar_pass(user):
    global useradmin
    for i in range(3):
        if input('Ingrese la contraseña: ') == useradmin.get(user):
            return True
        else:
            print('Error: contraseña incorrecta (intento %d de 3)\n\n' % (i+1))
