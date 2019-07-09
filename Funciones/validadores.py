# -- Import
import time
import re
from itertools import cycle

# -- Variables
lugares = {'ASIA': .7, 'AMERICA': .10, 'EUROPA': .14}
estados = ['NUEVO', 'USADO']
idiomas = ['ESPAÑOL', 'INGLES', 'FRANCES']

# -- Validador de datos de personas


def rut(rut):
    try:
        rut = rut.upper()
        rut = rut.replace("-", "")
        rut = rut.replace(".", "")
        aux = rut[:-1]
        dv = rut[-1:]
        reversed_digits = map(int, reversed(str(aux)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        resultado = (-s) % 11
        if str(resultado) == dv:
            return True
        elif dv == "K" and resultado == 10:
            return True
        else:
            return False
    except ValueError:
        print('Has ingresado un texto que no corresponde a un RUT')
    pass


def correo(valor):
    while True:
        if re.search('@', valor):
            return valor
        else:
            valor = input(
                'Error: Correo ingresado no es valido\nIngrese un correo valido: ')
    pass


def fecha(valor: str):
    while True:
        try:
            fecha = time.strptime(valor, '%d/%m/%Y')
            return valor
        except Exception as e:
            print('Error: Fecha ingresada no es valida\n')
            valor = input('Ingrese otra fecha (DD/MM/AAA): ')
    pass


def isbn(valor: int):
    while True:
        if len(valor) > 9:
            return valor
        else:
            valor = input(
                'Error: Ingrese un ISBN valido de 10/13 caracteres alphanúmericos\nISBN: ')


def lugar(valor_entrada: str):
    global lugares
    while True:
        valor = valor_entrada.upper()
        lugares_list = lugares.keys()
        if valor in lugares_list:
            return valor
        else:
            print('Error: La procedencia no existe en los registros')
            valor = input(
                'Ingrese una procedencia valida (America/Asia/Europa): ')
    pass


def estado(valor_entrada: str):
    global estados
    while True:
        valor = valor_entrada.upper()
        if valor in estados:
            return valor
        else:
            print('Este tipo de estado no existe en los registros')
            valor = input('Ingrese un estado valido (Nuevo/Usado): ')
    pass


def idioma(valor_entrada: str):
    global idiomas
    while True:
        valor = valor_entrada.upper()
        if valor in idiomas:
            return valor
        else:
            print('Este tipo de estado no existe en los registros')
            valor = input(
                'Ingrese un idioma valido (Español/Ingles/Frances): ')
    pass
