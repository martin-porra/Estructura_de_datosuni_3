class nodo:
    __objeto = None
    __siguiente = None

    def __init__(self,ob):
        self.__objeto = ob
        self.__siguiente = None

    def setsiguiente(self,sig):
        self.__siguiente = sig

    def getsiguiente(self):
        return self.__siguiente
    def getdato(self):
        return self.__objeto

class Lista:
    __cabeza = None
    __cant = None

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def insertar(self,x):
        aux = self.__cabeza
        nuevo = nodo(x)
        if aux == None:
            self.__cabeza =  nuevo
            nuevo.setsiguiente(None)
            self.__cant+=1
        elif int(aux.getdato().getaño()) > int(x.getaño()):
            nuevo.setsiguiente(aux)
            self.__cabeza = nuevo
            self.__cant += 1
        else:
            while aux.getsiguiente() != None and int(aux.getsiguiente().getdato().getaño()) < int(x.getaño()):
                aux = aux.getsiguiente()
            nuevo.setsiguiente(aux.getsiguiente())
            aux.setsiguiente(nuevo)
            self.__cant+=1

    def recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getdato().getcargo())
            aux = aux.getsiguiente()

    def cargo(self,cargo):
        aux = self.__cabeza
        año = 0
        cantidad = 0
        bandera = False
        while aux != None:
            if aux.getdato().getaño() == año:
                if aux.getdato().getcargo() == cargo:
                 cantidad = int(aux.getdato().getm()) + int(cantidad)
            else:
                if  bandera:
                 print('En el año {} hubo una cantidad de {} mujeres en el cargo de {}'.format(año, cantidad, cargo))
                 cantidad = 0
                año = aux.getdato().getaño()
                bandera = True
                if aux.getdato().getcargo() == cargo:
                 cantidad = aux.getdato().getm()
            aux = aux.getsiguiente()
        print('En el año {} hubo una cantidad de {} mujeres en el cargo de {}'.format(año, cantidad, cargo))


    def poraño(self,año,materia,cargo):
        aux = self.__cabeza
        cantidad= 0
        while aux != None:
            if aux.getdato().getaño() == año:
                if aux.getdato().getcargo().lower() == cargo.lower():
                    if aux.getdato().getmateria().lower() == materia.lower():
                        cantidad = int(cantidad) + int(aux.getdato().getm()) + int(aux.getdato().getv())
            aux = aux.getsiguiente()
        print('La cantidad de agentes designados en el año {}, en el cargo {} y la materia {} es: {} '.format(año,cargo,materia,cantidad) )