from Personal import Docente,Personal_apoyo,Investigador,Docente_investigador
from interface import IPersonal,ITesorero,IDirector
from interface import PosicionInvalidaException
from zope.interface import Interface, implementer
from zope.interface.exceptions import Invalid
import json
@implementer(IPersonal)
class Nodo:
    __personal: object
    __siguiente: object
    def __init__(self,personal):
        self.__personal = personal
        self.__siguiente = None
    def setsiguiente (self,siguiente):
        self.__siguiente = siguiente
    def getsiguiente (self):
        return self.__siguiente
    def getdato (self):
        return self.__personal
class Manejador_personal:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def insertarElemento(self, elemento, posicion):
        if posicion < 0 or posicion > self.__actual:
            raise PosicionInvalidaException("Posición inválida")

        if posicion == 0:
            self.__comienzo = Nodo(elemento, self.__comienzo)
        else:
            nodo_actual = self.__comienzo
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.getsiguiente()
            nuevo_nodo = Nodo(elemento, nodo_actual.getsiguiente())
            nodo_actual.setsiguiente(nuevo_nodo)
        self.__actual += 1
    def agregarElemento(self, elemento):
        self.insertarElemento(elemento, self.__actual)

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= self.__actual:
            raise PosicionInvalidaException("Posición inválida")

        nodo_actual = self.__comienzo
        for _ in range(posicion):
            nodo_actual = nodo_actual.getsiguiente()
        return nodo_actual.getdato()   
    def agregar_personal (self, personal):
        nodo = Nodo(personal)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def mostrar_docentes_investigadores(self,carrera):
        nodo_actual = self.__comienzo
        docentes = []
        while nodo_actual:
            personal = nodo_actual.getdato()
            if isinstance(personal, Docente_investigador) and personal.getcarrera() == carrera:
                docentes.append(personal)
            nodo_actual = nodo_actual.siguiente
        if docentes:
            ordenados = sorted(docentes)
            for docente in ordenados:
                print (docente)
        else: print(f"No se encontró ningun profesor que dicte la carrera '{carrera}'.")
    def cantidad_por_area (self,area):
        nodo_actual = self.__comienzo
        cont_doc = 0
        cont_inv = 0
        while nodo_actual:
            personal = nodo_actual.getdato()
            if isinstance(personal, Docente_investigador) and personal.getarea() == area:
                cont_doc += 1
            elif isinstance(personal, Investigador) and personal.getarea() == area:
                cont_inv += 1
        print (f"docentes investigadores en el area ingresada: {cont_doc}\n investigadores en el area ingresada: {cont_inv}\n")
    def listar (self):
        nodo_actual = self.__comienzo
        aux = []
        while nodo_actual:
            personal = nodo_actual.getdato()
            aux.append(personal)
        ordenados = sorted(aux)
        for personal in ordenados:
            clase = type(personal)
            sueldo = personal.calcular_sueldo()
            print (f"nombre: {personal.getnombre()}\n apellido: {personal.getapellido()}\n tipo: {clase.__name__}\n sueldo: {sueldo}")
    def mostrar_importe_extra (self,categoria):
        nodo_actual = self.__comienzo
        total = 0
        while nodo_actual:
            personal = nodo_actual.getdato()
            if isinstance(personal, Docente_investigador) and personal.getcategoria() == categoria:
                print (f"nombre: {personal.getnombre()}\n apellido: {personal.getapellido()}\n importe extra: {personal.getextra()}")
                total += personal.getextra()
        print (f"dinero que la secretaria necesitara para importes extra : {total}$")
    def buscar_por_dni (self,dni):
        encontrado = None
        nodo_actual = self.__comienzo
        total = 0
        while nodo_actual and encontrado == None:
                personal = nodo_actual.getdato()
                if personal.getdni() == dni:
                    encontrado = personal
        return encontrado
    def cargar_personal_desde_json(self):
        with open("personal.json") as archivo:
            datos = json.load(archivo)
        for personal_data in datos:
            if personal_data['tipo'] == 'Docente':
                personal = Docente(
                    personal_data['cuil'],
                    personal_data['apellido'],
                    personal_data['nombre'],
                    int(personal_data['sueldo']),
                    int(personal_data['antiguedad']),
                    personal_data['carrera'],
                    personal_data['cargo'],
                    personal_data['catedra']
                )
            elif personal_data['tipo'] == 'Personal_apoyo':
                personal = Personal_apoyo(
                    personal_data['cuil'],
                    personal_data['apellido'],
                    personal_data['nombre'],
                    int(personal_data['sueldo']),
                    int(personal_data['antiguedad']),
                    personal_data['categoria']
                )
            elif personal_data['tipo'] == 'Investigador':
                personal = Investigador(
                    personal_data['cuil'],
                    personal_data['apellido'],
                    personal_data['nombre'],
                    int(personal_data['sueldo']),
                    int(personal_data['antiguedad']),
                    personal_data['area'],
                    personal_data['tipo']
                )  
            elif personal_data['tipo'] == 'Docente_investigador':
                personal = Docente_investigador(
                    personal_data['cuil'],
                    personal_data['apellido'],
                    personal_data['nombre'],
                    int(personal_data['sueldo']),
                    int(personal_data['antiguedad']),
                    personal_data['carrera'],
                    personal_data['cargo'],
                    personal_data['catedra'],
                    personal_data['area'],
                    personal_data['tipo_investigacion'],
                    personal_data['categoria'],
                    int(personal_data['importe_extra'])
                )      
            self.agregarElemento(personal)
        archivo.close()
    def guardar_en_archivo(self):
        vehiculos = []
        for vehiculo in self:
            vehiculos.append(vehiculo.toJSON())
        with open('vehiculos.json', "w") as archivo:
            json.dump(vehiculos, archivo)
@implementer(ITesorero)
class Tesorero:
    def __init__(self, user, contraseña):
        self.__usuario = user
        self.__contraseña = contraseña

    def autenticar(self, user, contraseña):
        aux = False
        if self.__usuario == user:
            if self.__contraseña == contraseña:
                aux = True
            else: print ('contraseña invalida')
        else: print ('usuario invalido')
        return aux
    def gastosSueldoPorEmpleado(self,lista,dni):
        encontrado = lista.buscar_por_dni(dni)
        if encontrado:
            gastos = encontrado.calcular_sueldo()
            print(f"Gastos de sueldo para el empleado con DNI {dni}: {gastos}")
        else: print ('dni no encontrado\n')
@implementer(IDirector)
class Director:
    def __init__(self, user, contraseña):
        self.__usuario = user
        self.__contraseña = contraseña

    def autenticar(self, user, contraseña):
        aux = False
        if self.__usuario == user:
            if self.__contraseña == contraseña:
                aux = True
            else: print ('contraseña invalida')
        else: print ('usuario invalido')
        return aux
    def modificarBasico(self, dni,lista,nuevoBasico):
        encontrado = lista.buscar_por_dni(dni)
        if encontrado:
            encontrado.modificar_sueldo(nuevoBasico)
            print ('el sueldo basico se modifico con exito')
        else: print ('dni no encontrado\n')
    def modificarPorcentajeporcargo(self, dni,lista, nuevoPorcentaje):
        encontrado = lista.buscar_por_dni(dni)
        if encontrado:
            encontrado.modificar_porcentaje_categoria(nuevoPorcentaje)
            print ('el porcentaje por cargo se modifico con exito')
        else: print ('dni no encontrado\n')
    def modificarPorcentajeporcategoria(self, dni,lista, nuevoPorcentaje):
        encontrado = lista.buscar_por_dni(dni)
        if encontrado:
            encontrado.modificar_porcentaje_cargo(nuevoPorcentaje)
            print ('el porcentaje por cargo se modifico con exito')
        else: print ('dni no encontrado\n')

    def modificarImporteExtra(self, dni,lista, nuevoImporteExtra):
        encontrado = lista.buscar_por_dni(dni)
        if encontrado and isinstance(encontrado,Docente_investigador):
            encontrado.modificar_importe_extra(nuevoImporteExtra)
            print ('el porcentaje por cargo se modifico con exito')
        else: print ('dni no encontrado\n')
