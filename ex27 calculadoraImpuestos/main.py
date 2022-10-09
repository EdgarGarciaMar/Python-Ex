def pagoImpuestos(pago =0,impuesto=0):
    print(f'Pago sin impuesto ingresado= {pago}')
    print(f'Impuesto ingresado = {impuesto}')
    pagoTotal = pago+pago*(impuesto/100)
    print(f'Pago con impuesto = {pagoTotal}')


pago = float(input("Proporcione el pago sin impuesto = "))
impuesos = float(input("Proporcione el monto del impuesto = "))
print(" ")
pagoImpuestos(pago,impuesos)
