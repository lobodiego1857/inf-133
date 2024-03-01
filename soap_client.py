from zeep import Client

client = Client('http://localhost:8000/')

result = client.service.Saludar(nombre="Diego")
print(result)

result = client.service.SumaDosNumeros(num1=20, num2=23)
print(result)

cadena1 = "Lavan esa base naval"
result_palindromo1 = client.service.CadenaPalindromo(cadena=cadena1)
print(f"¿Es '{cadena1}' un palíndromo?: {result_palindromo1}")

cadena2 = "Alexander"
result_palindromo2 = client.service.CadenaPalindromo(cadena=cadena2)
print(f"¿Es '{cadena2}' un palíndromo?: {result_palindromo2}")