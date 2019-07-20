# -- Creación de la clase objeto persona


class persona(object):

    def __init__(self, rut, nombre, fecha_nacimiento, direccion_particular,
                 telefono, correo):
        self.rut = rut
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion_particular = direccion_particular
        self.telefono = telefono
        self.correo = correo
        pass

    def datos_completos(self):
        return print('Datos consultados:\n\n',
                     'Rut: ', self.rut, '\n',
                     'Nombre: ', self.nombre, '\n',
                     'Fecha de nacimiento: ', self.fecha_nacimiento, '\n',
                     'Dirección Particular: ', self.direccion_particular, '\n',
                     'Telefono: ', self.telefono, '\n',
                     'Correo Electronico: ', self.correo)
    