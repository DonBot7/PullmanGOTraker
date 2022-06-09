# PullmanGO Tracker
Simple tracker para telegram hecho en Python. Te ofrece mas informacion en tiempo real que el sitio oficial.


Instrucciones:
-------------

- Abre ```config.py ```
- instala las dependencias con ```pip install -r requirements.txt```
- En ```TOKEN=``` debes ingresar el token de tu bot de telegram.
- En ```chat_id=``` debes ingresar el id de donde quieres recibir la informacion. (id de tu user o de canal de telegram)


uso:
-------------
```python tracker.py -o <numero de envio> -n "nombre personalizado" -m <modo> -t <tiempo de request en segundos>```
 
 El modo puede ser "telegram" o "consola"
 
 - Telegram: te envia la info a tu telegram
 - Consola: solo imprime la informacion en la consola, sin enviar a telegram nada.
 
 El tiempo es opcional , solo requerido cuando envies la info a tu telegram.

Ejemplos: 
-------------
Con modo telegram:
 
![image](https://user-images.githubusercontent.com/13562845/172766185-37915182-7162-4e9b-9741-821cd6483cd2.png)
 
Con modo consola:
 
![image](https://user-images.githubusercontent.com/13562845/172765996-5ab27344-0cff-4488-8d1e-bce3c7b207e1.png)
