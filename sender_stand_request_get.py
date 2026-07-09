import requests # importa las funciones de request (get, post, update, delete, etc.)
import configuration # importa las variables del archivo configurarion.py (las rutas o paths que debo revisar)

def get_users_table(): # crea la funcion GET
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
    # le brinda a la funcion la ruta en la que debe aplicar la request

response = get_users_table() # llama a la funcion y le asigna un nombre
print(response.status_code) # muestra el codigo de status de la request
print(response.headers) # muestra los headers de la request

