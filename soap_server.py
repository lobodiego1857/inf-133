from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "Hola, {}!".format(nombre)

def suma_dos_numeros(num1, num2):
    return num1 + num2

def cadena_palindromo(cadena):
    cadena = ''.join(c for c in cadena if c.isalnum()).lower()
    return cadena == cadena[::-1]

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str},
)

dispatcher.register_function(
    "SumaDosNumeros",
    suma_dos_numeros,
    returns={"resultado": float},
    args={"num1": float, "num2": float},
)

dispatcher.register_function(
    "CadenaPalindromo",
    cadena_palindromo,
    returns={"es_palindromo": bool},
    args={"cadena": str},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciando en http://localhost:8000/")
server.serve_forever()
