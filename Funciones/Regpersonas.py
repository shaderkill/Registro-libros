import Funciones.validadores as validar
from Clases import personas
persona = personas.persona

personas_reg = {}

# -- Funciones

def listar_personas():
    print("\nPersonas Registradas: ")
    print("\n".join(personas_reg.values()))
    input("Presione una enter para volver")
    
          
def registrar_personas():
    global personas_reg
    rut = input('Ingrese el RUT de la persona (12345678-9): ')
    if validar.rut(rut):
        list_rut = personas_reg.keys()
        if rut not in list_rut:
            nombre = input('Ingrese el nombre de la persona: ')
            fecha = validar.fecha(input('Ingrese la fecha de nacimiento (DD/MM/AAAA): '))
            direccion = input('Ingrese la dirección particular: ')
            telefono = input('Ingrese el número de contacto: ')
            correo = validar.correo(input('Ingrese el correo electronico: '))
            personas_reg.setdefault(str(rut), nombre)
            rut = persona(rut, nombre, fecha, direccion, telefono, correo)
            rut.datos_completos()
            print('Persona registrada con exito')
            print('\n')
            input("Presione una enter para volver")
        else:
            print('Persona ya se encuentra registrada\n')
            input("Presione una enter para volver")
    else:
        print('RUT ingresado no es valido\n')
        registrar_personas()
    pass
