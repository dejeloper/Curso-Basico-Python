menu = """
Bienvenido al Conversor de monedas 💰😂

[1] Pesos Argentinos
[2] Pesos Colombianos
[3] Pesos Mexicanos

Elige una opción: """

option = input(menu)

if option == '1':
  pesos = float(input("¿Cuántos pesos Argentinos tienes?: "))
  valor_dolar = 70.66
  dolares = round(pesos / valor_dolar, 2)
  print("Tienes $" + str(dolares) + " dólares")
elif option == '2':
  pesos = float(input("¿Cuántos pesos Colombianos tienes?: "))
  valor_dolar = 3650.05
  dolares = round(pesos / valor_dolar, 2)
  print("Tienes $" + str(dolares) + " dólares")
elif option == '3':
  pesos = float(input("¿Cuántos pesos Mexicanos tienes?: "))
  valor_dolar = 22.39
  dolares = round(pesos / valor_dolar, 2)
  print("Tienes $" + str(dolares) + " dólares")
else:
  print('La opción seleccionada no es válida')


