from encapsulamiento import Person

if __name__ == "__main__":
    print("Creacion de objetos".center(50,"-")) #Caracteres para dar formato ---creacion de objetos---
    persona = Person("Karla","Gomez",20,"Lectura")
    persona.mostrarDetalle()
    #Se agrego el destructor en la clase de encapsulamiento
    print("Destruccion de objetos".center(50,"-"))
    del persona