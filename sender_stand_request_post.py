import requests # importa las funciones de request (get, post, update, delete, etc.)
import configuration # importa las variables del archivo configurarion.py (las rutas o paths que debo revisar)
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)