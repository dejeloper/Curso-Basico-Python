def es_primo(numero):
  if numero == 1:
    return False
  else:
    contador = 0
    for i in range(1, numero + 1):
      if numero % i == 0:
        contador +=1

    if contador > 2:
      return False
    else: 
      return True

def run():
  numero = int(input('Escribe un número: '))  
  if es_primo(numero):
    print('El número ' + str(numero) + ' Es primo')
  else:
    print('El número ' + str(numero) + ' No es primo')

if __name__ == "__main__":
  run()