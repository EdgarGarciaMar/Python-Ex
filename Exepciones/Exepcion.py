from NumerosIdenticos import NumerosIdenticos

resultado = None

try: #Todas las variables que se usan deben estar en este bloque
    a = int(input("a: "))
    b = int(input("b: "))
    if a == b:
        raise NumerosIdenticos("Numeros identicos") #Raise permite lanzar o arrojar una expecion
    resultado = a/b
except TypeError as e:
    print(f'Ocurrio un error TypeError: {e}, Type : {type(e)}')
except ZeroDivisionError as e:
    print(f'Ocurrio un error ZeroDivisionError: {e} , Type : {type(e)}')
except Exception as e:  # Clase BaseExeption y Exeption procesan todas las expeciones de las clases hijas como ZeroDivisionError
    print(f'Ocurrio un error Exception: {e} , Type : {type(e)}')
else: #SI NO OCURRE UNA EXPECION
    print("Else: NO SE  ARROJO NINGUNA EXPECION :)")
finally: #siempre se ejecuta incluso con expeciones
    print("Finally: Ejecucion siempre Finally...")

print(f'Resultado :{resultado}')
print("continuamos...")