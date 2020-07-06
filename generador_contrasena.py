import random
import string

def generar_contrasena():
  mayusculas = string.ascii_uppercase
  minusculas = string.ascii_lowercase
  simbolos = ['!', '#', '$', '/', '(', ')']
  numeros = string.digits  
  caracteres = mayusculas + minusculas + ''.join(simbolos) + numeros
  
  contrasena = []

  for i in range(15):
    caracter_random = random.choice(caracteres)
    contrasena.append(caracter_random)

  return ''.join(contrasena)

def run():
  contrasena = generar_contrasena()
  print('Tu nueva contraseña es: ' + contrasena)

if __name__ =="__main__":
  run()