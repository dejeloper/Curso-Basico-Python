def run(): 
  # # Uso de continue
  # for contador in range(1, 10):
  #   if(contador % 2 != 0):
  #     continue
  #   print(contador) 
  
  # # Uso de break
  # for i in range(10000):
  #   print(i)
  #   if i == 2400:
  #     break

  texto = str(input('Escriba un texto: ')).strip()
  for letra in texto:
    if letra == 'o':
      break
    print(letra)


if __name__ == "__main__":
  run()