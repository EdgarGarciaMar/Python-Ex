edad = int(input("""
    Proporciona tu edad
    Rango de 0-30 años:  
"""))

if edad >= 0 and edad < 10:
    print(f'{edad}: La infancia es increible')
elif edad >= 10 and edad < 20:
    print(f'{edad}: Muchos cambios y mucho estudio')
elif edad >= 20 and edad < 30:
    print(f'{edad}: Amor y comienza el trabajo')
else:
    print("Etapa de la vida no reconocida.")


