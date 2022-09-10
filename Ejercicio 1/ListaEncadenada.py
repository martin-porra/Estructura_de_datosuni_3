class Nodo:
    __dato = None
    __sig = None
    def __init__(self,dato):
        self.__dato = dato
        self.__sig = None
    def getDato(self):
        return self.__dato
    def setsiguiente(self,sig):
        self.__sig = sig
    def getsiguiente(self):
        return self.__sig
    def setdato(self,dato):
        self.__dato = dato
class ListaEncadenada:
    __comienzo = None
    __ul = None

    def __init__(self):
        self.__comienzo = None
        self.__ul = 0

    def insertar(self,x,p):
        nuevo = Nodo(x)
        if isinstance(x,int):
            aux = self.__comienzo
            if p-1 == 0:
                self.__comienzo = nuevo
                nuevo.setsiguiente(aux)
                self.__ul+=1
            if p-1 > 0 and p-1 < self.__ul+1:
                i=1
                ant = aux
                aux = aux.getsiguiente()
                while i !=p-1 and aux != None:
                    ant = aux
                    aux = aux.getsiguiente()
                    i+=1
                ant.setsiguiente(nuevo)
                nuevo.setsiguiente(aux)
                self.__ul+=1
            if p-1 > self.__ul+1:
                print('Posicion invalida')

    def insertarContenido(self,x):
        nuevo= Nodo(x)
        aux = self.__comienzo
        if self.__comienzo == None:
            self.__comienzo= nuevo
            self.__ul += 1
        elif aux.getDato() > x:
                nuevo.setsiguiente(aux)
                self.__comienzo = nuevo
                self.__ul += 1
        else:

            while aux.getsiguiente() != None and aux.getsiguiente().getDato() < x:
                aux = aux.getsiguiente()

            nuevo.setsiguiente(aux.getsiguiente())
            aux.setsiguiente(nuevo)
            self.__ul += 1
    def suprimir(self,p):
     aux = self.__comienzo
     if not self.vacia():
        if p-1 == 0:
            self.__comienzo=  self.__comienzo.getsiguiente()
            self.__ul-=1
        if p-1 > 0 and p-1 < self.__ul:
            i=1
            ant = aux
            aux= aux.getsiguiente()
            while i!= p-1 and aux!=None:
                ant = aux
                aux = aux.getsiguiente()
                i+=1
            ant.setsiguiente(aux.getsiguiente())
            self.__ul-=1
     else:
         print('lista Vacia')
    def vacia(self):
        return (self.__ul == 0)


    def recorrer(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getsiguiente()




