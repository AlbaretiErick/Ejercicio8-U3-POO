class Personal:
    def __init__(self,dni,cuil,apellido,nombre,sueldo,ant):
        self.__dni = dni
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo = sueldo 
        self.__antiguedad = ant
    def __lt__ (self,otro):
        return (self.__apellido.lower(),self.__nombre.lower()) < (otro.getapellido().lower(),otro.getnombre().lower())
    def __str__(self):
        return f"CUIL: {self.__cuil}\nApellido: {self.__apellido}\nNombre: {self.__nombre}\nSueldo: {self.__sueldo}\nAntigüedad: {self.__antiguedad}"
    def getnombre (self):
        return self.__nombre
    def getapellido (self):
        return self.__apellido
    def getdni (self):
        return self.__dni
    def calcular_sueldo (self):
        return self.__sueldo + self.calcular_aumento_antiguedad()
    def calcular_aumento_antiguedad(self):
        return self.__sueldo * (self.__antiguedad * 0.01)
    def modificar_sueldo(self,nuevo):
        self.__sueldo = nuevo
    def toJSON (self):
        return {
            'cuil': self.__cuil,
            'apellido': self.__apellido,
            'nombre': self.__nombre,
            'sueldo': self.__sueldo,
            'antiguedad': self.__antiguedad
        }
class Docente(Personal):
    def __init__(self, dni, cuil, apellido, nombre, sueldo, ant, carrera, cargo, catedra):
        super().__init__(dni, cuil, apellido, nombre, sueldo, ant)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    def getcarrera (self):
        return self.__carrera
    def getcargo (self):
        return self.__cargo
    def getcatedra (self):
        return self.__catedra
    def __str__(self):
        return f"{super().__str__()}\nCarrera: {self.__carrera}\nCargo: {self.__cargo}\nCátedra: {self.__catedra}"
    def calcular_sueldo(self):
        sueldo = super().calcular_sueldo()
        return sueldo + self.calcular_aumento_cargo()

    def calcular_aumento_cargo(self):
        if self.__cargo == "simple":
            return self.__sueldo * 0.1
        elif self.__cargo == "semiexclusivo":
            return self.__sueldo * 0.2
        elif self.__cargo == "exclusivo":
            return self.__sueldo * 0.5
    def toJSON(self):
        d = super().toJSON()
        d['carrera'] = self.__carrera
        d['cargo'] = self.__cargo
        d['catedra'] = self.__catedra
        return d
class Personal_apoyo(Personal):
    def __init__(self, dni, cuil, apellido, nombre, sueldo, ant, categoria):
        super().__init__(dni, cuil, apellido, nombre, sueldo, ant)
        self.__categoria = categoria
    def __str__(self):
        return f"{super().__str__()}\nCategoría: {self.__categoria}"
    def calcular_sueldo(self):
        sueldo = super().calcular_sueldo()
        return sueldo + self.calcular_aumento_categoria()

    def calcular_aumento_categoria(self):
        if self.__categoria in range(1, 11):
            return self.__sueldo * 0.1
        elif self.__categoria in range(11, 21):
            return self.__sueldo * 0.2
        elif self.__categoria in range(21, 23):
            return self.__sueldo * 0.3
    def toJSON(self):
        d = super().toJSON()
        d['categoria'] = self.__categoria
        return d
class Investigador(Personal):
    def __init__(self, dni, cuil, apellido, nombre, sueldo, ant, area, tipo):
        super().__init__(dni, cuil, apellido, nombre, sueldo, ant)
        self.__area = area
        self.__tipo_investigacion = tipo
    def getarea (self):
        return self.__area
    def gettipo (self):
        return self.__tipo_investigacion
    def __str__(self):
        return f"{super().__str__()}\nÁrea: {self.__area}\nTipo de investigación: {self.__tipo_investigacion}"
    def toJSON(self):
        d = super().toJSON()
        d['area'] = self.__area
        d['tipo'] = self.__tipo_investigacion
        return d
class Docente_investigador(Docente, Investigador):
    def __init__(self, dni, cuil, apellido, nombre, sueldo, ant, carrera, cargo, catedra, area, tipo,categoria,extra):
        Docente.__init__(self, dni, cuil, apellido, nombre, sueldo, ant, carrera, cargo, catedra)
        Investigador.__init__(self, dni, cuil, apellido, nombre, sueldo, ant, area, tipo)
        self.__categoria = categoria
        self.__importe_extra = extra
    def getcategoria (self):
        return self.__categoria
    def getextra (self):
        return self.__importe_extra
    def __str__(self):
        return f"{super().__str__()}\nCarrera: {self.__carrera}\nCargo: {self.__cargo}\nCátedra: {self.__catedra}\nÁrea: {self.__area}\nTipo de investigación: {self.__tipo_investigacion}\nCategoría: {self.__categoria}\nImporte extra: {self.__importe_extra}"
    def calcular_sueldo(self):
        sueldo = super(Docente, self).calcular_sueldo()  
        sueldo += self.__importe_extra  
        return sueldo
    def modificar_importe_extra (self,nuevo):
        self.__importe_extra = nuevo
    def toJSON(self):
        d = super().toJSON()
        d['area'] = self.__area
        d['tipo'] = self.__tipo_investigacion
        d['categoria'] = self.__categoria
        d['importe_extra'] = self.__importe_extra
        return d
        