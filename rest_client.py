import requests

url = "http://localhost:8000/"

# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Diego",
    "apellido": "Cruz",
    "carrera": "Informatica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

ruta_buscar_nombre = url + "buscar_nombre"
buscar_nombre_response = requests.request(method="GET", url=ruta_buscar_nombre)
print("\nRespuesta GET /buscar_nombre:")
print(buscar_nombre_response.text)

ruta_contar_carreras = url + "contar_carreras"
conteo_response = requests.request(method="GET", url=ruta_contar_carreras)
print("\nRespuesta GET /contar_carreras:")
print(conteo_response.text)

ruta_total_estudiantes = url + "total_estudiantes"
total_estudiantes_response = requests.request(method="GET", url=ruta_total_estudiantes)
print("\nRespuesta GET /total_estudiantes:")
print(total_estudiantes_response.text)