def run():
  frase = str(input("Escriba una frase: ")).strip()
  for caracter in frase:
    print(caracter.upper())

if __name__ == "__main__":
  run()