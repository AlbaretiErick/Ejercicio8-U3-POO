from Lista import Manejador_personal,Tesorero,Director
from Personal import Docente,Personal_apoyo,Investigador,Docente_investigador
mn_personal = Manejador_personal()
mn_personal.cargar_personal_desde_json()
tesorero = Tesorero("uTesoreso", "ag@74ck")
director = Director("uDirector", "ufC77#!1")
while True:
        print ("opcion 1:  Insertar a agentes a la colección.")
        print ("opcion 2: Agregar agentes a la colección.")
        print ("opcion 3:  Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.")
        print ("opcion 4:  Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
        print ("opcion 5: Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.")
        print ("opcion 6: Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
        print ("opcion 7: Dada una categoría de investigaciónlistar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría y mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.")
        print ("opcion 8: Almacenar los datos de todos los agentes en el archivo “personal.json")
        print ("opcion 9: ingresar como tesorero")
        print ("opcion 10: ingresar como director")
        print ("opcion 11: salir")
        opcion = input ("ingresar opcion \n")
        if opcion == '1':
            tipo_personal = input("Ingrese el tipo de personal: \n")
            cuil = int(input("Ingrese el cuil: \n"))
            apellido = input("Ingrese el apellido: \n")
            nombre = input("Ingrese el nombre: \n")
            sueldo = int(input("Ingrese el sueldo: \n"))
            antiguedad = input("Ingrese la antiguedad: \n")

            if tipo_personal == "Docente":
                carrera = input("Ingrese la carrera en la que dicta clases: \n")
                cargo = input("Ingrese el cargo: \n")
                catedra = input("Ingrese la catedra: \n")
                personal = Docente(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra)
            elif tipo_personal == "Personal de apoyo":
                categoria = input("Ingrese la categoria: \n")
                personal = Personal_apoyo(cuil,apellido,nombre,sueldo,antiguedad,categoria)
            elif tipo_personal == "Investigador":
                area = input("Ingrese el area: \n")
                tipo = input("Ingrese el tipo de investigacion: \n")
                personal = Investigador(cuil,apellido,nombre,sueldo,antiguedad,area,tipo)
            else:
                carrera = input("Ingrese la carrera en la que dicta clases: \n")
                cargo = input("Ingrese el cargo: \n")
                catedra = input("Ingrese la catedra: \n")
                area = input("Ingrese el area: \n")
                tipo = input("Ingrese el tipo de investigacion: \n")
                categoria = input("Ingrese la categoria en el programa: \n")
                extra = input("Ingrese el importe extra: \n")
                personal = Docente_investigador(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,area,tipo,categoria,extra)
            pos = input ('ingresar posicion: \n')
            mn_personal.intertarElemento(pos,personal)
        if opcion == '2':
            tipo_personal = input("Ingrese el tipo de personal: \n")
            cuil = int(input("Ingrese el cuil: \n"))
            apellido = input("Ingrese el apellido: \n")
            nombre = input("Ingrese el nombre: \n")
            sueldo = int(input("Ingrese el sueldo: \n"))
            antiguedad = input("Ingrese la antiguedad: \n")

            if tipo_personal == "Docente":
                carrera = input("Ingrese la carrera en la que dicta clases: \n")
                cargo = input("Ingrese el cargo: \n")
                catedra = input("Ingrese la catedra: \n")
                personal = Docente(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra)
            elif tipo_personal == "Personal de apoyo":
                categoria = input("Ingrese la categoria: \n")
                personal = Personal_apoyo(cuil,apellido,nombre,sueldo,antiguedad,categoria)
            elif tipo_personal == "Investigador":
                area = input("Ingrese el area: \n")
                tipo = input("Ingrese el tipo de investigacion: \n")
                personal = Investigador(cuil,apellido,nombre,sueldo,antiguedad,area,tipo)
            else:
                carrera = input("Ingrese la carrera en la que dicta clases: \n")
                cargo = input("Ingrese el cargo: \n")
                catedra = input("Ingrese la catedra: \n")
                area = input("Ingrese el area: \n")
                tipo = input("Ingrese el tipo de investigacion: \n")
                categoria = input("Ingrese la categoria en el programa: \n")
                extra = input("Ingrese el importe extra: \n")
                personal = Docente_investigador(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,area,tipo,categoria,extra)
            mn_personal.agregarElemento(personal)
        if opcion == '3':
            pos = input ('ingresar posicion: \n')
            mn_personal.mostrarElemento(pos)
        elif opcion == '4':
            carrera = input ('ingresar carrera: \n')
            mn_personal.mostrar_docentes_investigadores(carrera)
        elif opcion == '5':
            area = input ('ingresar area: \n')
            mn_personal.cantidad_por_area(area)
        elif opcion == '6':
            mn_personal.listar()
        elif opcion == '7':
            categoria = input ('ingresar categoria: \n')
            mn_personal.mostrar_importe_extra(categoria)
        elif opcion == '8':
            mn_personal.guardar_en_archivo()
        elif opcion == '9':
            user = input ('ingresar usuario: \n')
            code = input ('ingresar contraseña: \n')
            if tesorero.autenticar(user,code):
                print("Autenticación exitosa como Tesorero")
                confirmacion = True
                while confirmacion:
                    dni = input("Ingrese el DNI del empleado: ")
                    tesorero.gastosSueldoPorEmpleado(mn_personal,dni)
                    si = input ('¿quiere verificar los gastos de otro dni?\n')
                    if si != 'si':
                        confirmacion = False
                    
        elif opcion == '10':
            user = input ('ingresar usuario: \n')
            code = input ('ingresar contraseña: \n')
            if director.autenticar(user,code):
                print ("Autenticación exitosa como director")
                while True:
                    print ("opcion 1: Modificar sueldo básico ")
                    print ("opcion 2: Modificar porcentaje por cargo")
                    print ("opcion 3: Modificar porcentaje por categoría")
                    print ("opcion 4: Modificar importe extra")
                    print ("opcion 5: salir")
                    opcion = input ('ingresar opcion:\n')
                    if opcion == "1":
                        dni = input("Ingrese el DNI del agente: ")
                        nuevo = float(input("Ingrese el nuevo sueldo básico:\n"))
                        director.modificarBasico(dni,mn_personal,nuevo)
                    elif opcion == "2":
                        dni = input("Ingrese el DNI del agente: ")
                        nuevo = float(input("Ingrese el nuevo porcentaje por cargo:\n"))
                        director.modificarPorcentajeporcargo(dni,mn_personal, nuevo)
                    elif opcion == "3":
                        dni = input("Ingrese el DNI del agente: ")
                        nuevo = float(input("Ingrese el nuevo porcentaje por categoría:\n"))
                        director.modificarPorcentajeporcategoria(dni, nuevo)
                    elif opcion == "4":
                        dni = input("Ingrese el DNI del agente: ")
                        nuevo = float(input("Ingrese el nuevo importe extra:\n"))
                        director.modificarImporteExtra(dni, nuevo)
                    elif opcion == '5':
                        break
                    else:
                        print("Opción inválida")
        elif opcion == '11':
            break
        else: print ("opcion incorrecta")