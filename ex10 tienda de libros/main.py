print("Proporcione los siguientes datos del libro:")
nombreLibro = input("Proporciona El nombre del libro:")
idLibro = int(input("Proporciona el ID:"))
precioLibro = float(input("Proporciona el precio:"))
envioLibro = input("Indica si el envio es gratuito (True/False):")
tipoEnvio= "Envio Gratuito"

#Impresion multiple con formatos
print(f'''
  Nombre: {nombreLibro}
  ID: {idLibro}
  Precio: {precioLibro}
''')
if envioLibro == 'True':
  print(f'Tipo de envio:{tipoEnvio}')
else:
    tipoEnvio = "Envio con costo"
    print(f'Tipo de envio:{tipoEnvio}')


