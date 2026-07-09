import sender_stand_request_post
import sender_stand_request_get
import data

# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_user_body(first_name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable user_response
    user_response = sender_stand_request_post.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # Comprobar que el resultado de la solicitud se guarda en users_table_response
    users_table_response = sender_stand_request_get.get_users_table()

    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1

# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_symbol(first_name):
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado se guarda en la variable user_response
    user_response = sender_stand_request_post.post_new_user(user_body)

    # Comprueba si el código de estado es 400
    assert user_response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert user_response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert user_response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."

# Función de prueba negativa cuando el error es "No se han aprobado todos los parámetros requeridos"
def negative_assert_no_firstname(user_body):
    # El resultado se guarda en la variable user_response
    user_response = sender_stand_request_post.post_new_user(user_body)

    # Comprueba si el código de estado es 400
    assert user_response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert user_response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert user_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

    # Prueba 1. Usuario o usuaria creada con éxito. El parámetro firstName contiene 2 caracteres
def test_create_user_2_letter_in_first_name_get_success_response():
        positive_assert("Aa")

    # Prueba 2. Error. El parámetro firstName contiene 1 carácter
def test_create_user_1_letter_in_first_name_get_error_response():
        negative_assert_symbol('A')

    # Prueba 3. Error. El parámetro firstName contiene 16 caracteres
def test_create_user_16_letter_in_first_name_get_error_response():
        negative_assert_symbol('Aaaaaaaaaaaaaaaa')

    # Prueba 4. Error. El parámetro firstName contiene un espacio
def test_create_user_has_space_in_first_name_get_error_response():
        negative_assert_symbol('A Aaa')

    # Prueba 5. Error. El parámetro firstName contiene un string de caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
        negative_assert_symbol("\"№%@\",")

    # Prueba 6. Error. El parámetro firstName contiene un string de dígitos
def test_create_user_has_number_in_first_name_get_error_response():
        negative_assert_symbol("123")

    # Prueba 7. Error. Falta el parámetro firstName en la solicitud
def test_create_user_no_first_name_get_error_response():
        # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
        user_body = data.user_body.copy()
        # El parámetro "firstName" se elimina de la solicitud
        user_body.pop("firstName")
        # Comprueba la respuesta
        negative_assert_no_firstname(user_body)

    # Prueba 8. Error. El parámetro contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
        # El cuerpo actualizado de la solicitud se guarda en la variable user_body
        user_body = get_user_body("")
        # Comprueba la respuesta
        negative_assert_no_firstname(user_body);