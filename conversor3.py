def conversor(tipo_peso, valor_dolar):
  pesos = float(input("¿Cuántos pesos " + tipo_peso + " tienes?: "))
  dolares = round(pesos / valor_dolar, 2)
  print("Tienes $" + str(dolares) + " dólares")

menu = """Bienvenido al Conversor de monedas 💰😂

[1] Pesos Argentinos
[2] Pesos Colombianos
[3] Pesos Mexicanos

Elige una opción: """

option = input(menu)

if option == '1':
  conversor("Argentinos", 70.66)
elif option == '2':
  conversor("Colombianos", 3650.05)
elif option == '3':
  conversor("Mexicanos", 22.39)
else:
  print('La opción seleccionada no es válida')


