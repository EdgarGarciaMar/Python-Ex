calificacion = int(input("""
    Ingresa la calificacion del alumno:
"""))
mensaje = None

if 0 <= calificacion < 6:
    mensaje= "F"
elif 6 <= calificacion < 7:
    mensaje="D"
elif 7 <= calificacion < 8:
    mensaje = "C"
elif 8 <= calificacion < 9:
    mensaje = "B"
elif 9 <= calificacion <= 10:
    mensaje = "A"
else:
    print("Calificacion no valida.")
print(f'la nota es -{mensaje}-')
