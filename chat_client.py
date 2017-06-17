# -*- coding: utf-8 -*-
u"""Chat Game.

Juego a modo de practica para la creación y lectura de
archivos JSON emulando un chat.

Participantes: Leonel y Kristian.

Fecha: 16-06-2017

"""

# Importamos la libreria para manejar JSON
import json
# Importamos la libreria para manejar fechas
from datetime import datetime
# Importamos la libreria para rutas de archivos
from os import path


def genera_archivo_json(diccionario, nombre_archivo):
    """Genera el archivo que contendra los objetos JSON."""
    with open(nombre_archivo, 'w') as archivo:
        return json.dump(diccionario, archivo, indent=4)


def lee_archivo_json(nombre_archivo):
    """Lee archivo y devuelve su contenido."""
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)


def genera_chat():
    """Retorna diccionario con valores que conforman el chat."""
    nombre_archivo = 'chat.json'
    ruta_archivo = '../' + nombre_archivo
    autor = 'Leonel'
    fecha_actual = str(datetime.now().date())

    if not path.exists(ruta_archivo):
        print 'No existen conversaciones anteriores.'
        mensaje = raw_input('Escriba su mensaje: ')
        chat_dia = {'nombre_autor': autor, 'mensaje': mensaje}
        chat_lista = [{'chat_fecha': fecha_actual, 'chat': [chat_dia]}]
        chat_contenedor = {'chat_game': chat_lista}
        genera_archivo_json(chat_contenedor, ruta_archivo)
    else:
        print 'Mensajes contenidos en: ' + nombre_archivo
        chat_contenedor = lee_archivo_json(ruta_archivo)

        for x in chat_contenedor['chat_game']:
            print '***********************'
            print x['chat_fecha']
            print '-----------------------'

            for z in x['chat']:
                print z['nombre_autor'] + ' -> ' + z['mensaje']

genera_chat()
