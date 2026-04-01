def registrar_estudiante():

    nombre = input("ingresa el nombre del estudiante: ")

    i = 0
    while True:
        try: 
            edad = int (input ("ingresa la edad del estudiante: "))
            if edad < i:
                print("ingrese un valor valido")  
                continue
            break

        except ValueError:
            print("ingrese solo numeros")


    identificacion = input ("ingresa el id: ")

    curso = input ("escribe curso o programa: ")

    estado = input ("activo o inactivo: ") 
    if estado == 'activo':
        print(" estado registrado correctamente")
    elif estado == 'inactivo':
         print(" estado registrado correctamente")

    else:
        print("no es un valor valido")

        data = {
            "nombre": nombre,
            

    
}