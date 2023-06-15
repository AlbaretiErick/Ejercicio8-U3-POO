from zope.interface import Interface, implementer
from zope.interface.exceptions import Invalid

class PosicionInvalidaException(Exception):
    pass
class AutenticacionException(Exception):
    pass
class IPersonal(Interface):
    def insertarElemento(elemento, posicion):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(posicion):
        pass
class ITesorero(Interface):
    def gastosSueldoPorEmpleado(dni):
        pass

class IDirector(Interface):
    def modificarBasico(dni, nuevoBasico):
        pass
    
    def modificarPorcentajeporcargo(dni, nuevoPorcentaje):
        pass
    
    def modificarPorcentajeporcategoría(dni, nuevoPorcentaje):
        pass
    
    def modificarImporteExtra(dni, nuevoImporteExtra):
        pass
