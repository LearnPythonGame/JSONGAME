# -*- coding: utf-8 -*-
u"""Script Game.

Juego a modo de practica para la creación y lectura de
archivos JSON.

Participantes: Leonel y Kristian.

Fecha: 13-06-2017

"""

# Importamos la libreria para manejar JSON
import json
# Objeto que nos permitira elegir un numero aleatorio
from random import randrange


def clasificador(clave, valor):
    """Retorna diccionario con valores aleatorios."""
    clasificacion = dict()
    for i in clave:
        cantidad = len(valor)
        v = randrange(cantidad)
        clasificacion[i] = valor.pop(v)
    return clasificacion


def genera_archivo_json(clave, valor, nombre_archivo):
    """Genera el archivo que contendra los objetos JSON."""
    with open(nombre_archivo, 'w') as archivo:
        return json.dump(clasificador(clave, valor), archivo, indent=4)


def lee_archivo_json(nombre_archivo):
    """Lee archivo y devuelve su contenido."""
    with open(nombre_archivo, 'r') as archivo:
        contenido = json.load(archivo)
    print contenido

# datos para el ejemplo
aspirantes = [
    'Leonel',
    'Kristian',
    'Eveli',
    'Delia',
    'Wuilliam',
    'Jesenia',
    'Miguel',
    'Zoliyer',
    'Yuliana'
]
posicion = [
    'Coordinador',
    'Secretario',
    'Tesorero',
    'Contralor',
    'Educacion',
    'Eliminado 1',
    'Eliminado 2',
    'Eliminado 3',
    'Eliminado 4',
]

# preguntamos al usuario que desea hacer
opcion = raw_input('Generar archivo: 1, Leer archivo: 2 ¿1 o 2?')

# Evaluamos la respuesta del usuario
if opcion == "1":
    genera_archivo_json(posicion, aspirantes, 'coop.json')
    print u"Archivo generado"
elif opcion == "2":
    lee_archivo_json('coop.json')
else:
    print u"Solo puede ingresar el número 1 o el número 2"
