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
from datetime import date
# Importamos la libreria para rutas de archivos
from os import path


# Variables generales
nombre_archivo = 'chat.json'
ruta_archivo = '../' + nombre_archivo
autor = 'Leonel'
fecha_actual = date.today().strftime("%d-%m-%Y")


def genera_archivo_json(diccionario, nombre_archivo):
    """Genera el archivo que contendra los objetos JSON."""
    with open(nombre_archivo, 'w') as archivo:
        return json.dump(diccionario, archivo, indent=4)


def lee_archivo_json(nombre_archivo):
    """Lee archivo y devuelve su contenido."""
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)


def ver_chat(ruta_archivo, nombre_archivo):
    """Permite visualizar el chat contenido en el objeto JSON."""
    chat_contenedor = lee_archivo_json(ruta_archivo)

    print ''
    print 'Mensajes contenidos en: ' + nombre_archivo
    for x in chat_contenedor['chat_game']:
        print '***********************'
        print x['chat_fecha']
        print '-----------------------'

        for z in x['chat']:
            print z['nombre_autor'] + ' -> ' + z['mensaje']


def actualiza_chat(nombre_archivo, autor, fecha_actual):
    """Permite generar nuevos mensajes o nuevos chat."""
    chat_contenedor = lee_archivo_json(nombre_archivo)
    print '+++++++++++++++++++++++'
    mensaje = raw_input('Escriba su mensaje: ')
    chat_dia = {'nombre_autor': autor, 'mensaje': mensaje}

    ultima_fecha = chat_contenedor['chat_game'][-1]['chat_fecha']
    if ultima_fecha == fecha_actual:
        chat_contenedor['chat_game'][-1]['chat'].append(chat_dia)
    else:
        chat_lista = {'chat_fecha': fecha_actual, 'chat': [chat_dia]}
        chat_contenedor['chat_game'].append(chat_lista)
    genera_archivo_json(chat_contenedor, nombre_archivo)


def interaccion_chat(nombre_archivo, ruta_archivo, autor, fecha_actual):
    u"""Brinda interacción para chatear."""
    while True:
        ver_chat(ruta_archivo, nombre_archivo)

        print '_______________________'
        opcion = raw_input('Desea escribir un nuevo mensaje? (s): ')
        if opcion == 's':
            actualiza_chat(ruta_archivo, autor, fecha_actual)
        else:
            print ''
            print 'ha salido del chat!'
            break


def gestiona_chat(ruta_archivo, nombre_archivo, autor, fecha_actual):
    """Genera, visualiza y actualiza el chat."""
    if not path.exists(ruta_archivo):
        print 'No existen conversaciones anteriores.'
        mensaje = raw_input('Escriba su mensaje: ')
        chat_dia = {'nombre_autor': autor, 'mensaje': mensaje}
        chat_lista = {'chat_fecha': fecha_actual, 'chat': [chat_dia]}
        chat_contenedor = {'chat_game': [chat_lista]}
        genera_archivo_json(chat_contenedor, ruta_archivo)
        interaccion_chat(nombre_archivo, ruta_archivo, autor, fecha_actual)
    else:
        interaccion_chat(nombre_archivo, ruta_archivo, autor, fecha_actual)

while True:
    print ''
    print 'Opciones de la aplicacion'
    print '-------------------------'
    print '1 - Solo ver el chat.'
    print '2 - Solo enviar un mensaje.'
    print '3 - Uso completo del chat.'
    print u'4 - Salir de la aplicación.'
    print ''
    accion = raw_input('Su opción: ')

    if accion == '1':
        if not path.exists(ruta_archivo):
            print ''
            print u'No se ha iniciado ningún chat, lo siento!'
            continue
        else:
            print ''
            ver_chat(ruta_archivo, nombre_archivo)
            print ''
            opcion = raw_input('Desea volver al menú? (s): ')

            if opcion == 's':
                continue
            else:
                print ''
                print u'ha salido de la aplicación, adios!'
                break
    elif accion == '2':
        if not path.exists(ruta_archivo):
            print ''
            print u'No se ha iniciado ningún chat, lo siento!'
            continue
        else:
            print ''
            actualiza_chat(ruta_archivo, autor, fecha_actual)
            print ''
            opcion = raw_input('Desea volver al menú? (s): ')

            if opcion == 's':
                continue
            else:
                print ''
                print u'ha salido de la aplicación, adios!'
                break
    elif accion == '3':
        print ''
        gestiona_chat(ruta_archivo, nombre_archivo, autor, fecha_actual)
    elif accion == '4':
        print ''
        print u'ha salido de la aplicación, adios!'
        break
    else:
        print ''
        print 'Solo puede ingresar opciones del 1 al 4'
