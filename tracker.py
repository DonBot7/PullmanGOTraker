import requests
import json
import pandas as pd
import time as t 
from config import TOKEN
from config import chat_id
import argparse



try:

    #se requiere de los argumentos.
    parser = argparse.ArgumentParser(description='Pullman Cargo Tracker')
    parser.add_argument('-o', '--odt', type=str , help='Orden de seguimiento ODT', required=True)
    parser.add_argument('-n', '--nombre', type=str , help='Nombre de la encomienda', required=True)
    parser.add_argument('-m', '--modo', type=str, help='Modo (consola/telegram)',required=True)
    parser.add_argument('-t', '--tiempo', type=int, help='cada cuanto tiempo (en segundos) quieres que te llegue la informaicon ',required=False)
    args = parser.parse_args()

    #se suministra la url
    url = 'http://www.pullmancargo.cl/WEB/cuentacorrientecarga/funciones/ajax.php?op=consultaodt&odt=' + args.odt

    respuesta = requests.get(url)
    data = respuesta.json()
    data_json = json.dumps(data)
    data_df = pd.read_json(data_json)

    estadodetalle = data_df.iloc[0]['ESTADO']
    agencia = data_df.iloc[0]['AGENCIA']
    estado = data_df.iloc[0]['estadoweb']
    fecha = data_df.iloc[0]['fechaf']
    hora = data_df.iloc[0]['hora']

    text_estado =""
    if estado == "ENCOMINEDA EN ESPERA DE RETIRO":
        text_estado = "Encomienda en espera de retiro 🕓"
    elif estado == "ENCOMIENDA RETIRADA":
        text_estado = "Encomienda retirada 📦"
    elif estado =="CLASIFICADO EN BODEGA":
        text_estado = "Encomienda en proceso de clasificación 📝"
    elif estado == "ENCOMIENDA EN PREPARACIÓN":
        text_estado = "Encomienda en preparación 📦"
    elif estado == "En Viaje entre regiones":
        text_estado = "Encomienda viajando entre regiones 🚚"
    elif estado == "ENCOMIENDA EN REPARTO":
        text_estado = "Encomienda en reparto 🚚"
    elif estado == "ENCOMIENDA ENTREGADA":
        text_estado = "Encomienda entregada ✅"
    elif estado == "Venta":
        text_estado = "Encomienda vendida 💰"
    elif estado == "En Viaje entre agencias":
        text_estado = "Encomienda viajando entre agencias 🚚"
    elif estado == "Recepcionado en Agencia":
        text_estado = "Encomienda recepcionada en agencia 📦"
    elif estado =="En proceso de despacho":
        text_estado = "Encomienda en proceso de despacho 📦"
    elif estado == "Procesando para envio":
        text_estado = "Encomienda en proceso de envío 📦"


    text =  args.nombre + "\n" +"Agencia: " + agencia + "\n" + "Estado: " + text_estado + "\n("+ estado+ ", "+ estadodetalle +")\n "+"\n" + "Ultima actualizacion: " + hora + " " + fecha 
    url = 'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'

    #send r every 10 minute forever
    if  args.modo == "telegram":
        while True:
            r = requests.get(url.format(TOKEN=TOKEN, chat_id=chat_id, text=text))
            t.sleep(args.tiempo)
    elif args.modo == "consola":
        print(text)
 


        
except KeyboardInterrupt:
    print("\nHasta la próxima!")




