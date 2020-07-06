def palindromo(palabra):
  palabra = palabra.lower()
  print(palabra)
  if palabra[::-1] == palabra:
    return True
  else:
    return False

def run():
  palabra = input("Escribe una palabra: ").replace(' ', '')
  if palindromo(palabra):
    print("Es palíndromo")
  else:
    print("No es palíndromo")

if __name__ == "__main__":
  run()