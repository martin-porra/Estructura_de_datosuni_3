import numpy as np
class Lista:
    __arreglo = None
    __cant = None
    __maxima = None

    def __init__(self,max=10):
        self.__arreglo = np.empty(max,dtype=int)
        self.__maxima = max
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    def llena(self):
        return self.__cant == self.__maxima
    def insertar(self,x,p):
        if not self.llena():
          if p-1 >= 0 and p-1 <= self.__cant+1:
                    self.shift(p-1)
                    self.__arreglo[p-1] = x
                    self.__cant += 1
          else:
              print('Posicion invalida')
    def shift(self,i):
        for i in range(self.__cant,i,-1):
            self.__arreglo[i] = self.__arreglo[i-1]
    def rshift(self,i):
        for i in range(i,self.__cant,1):
            self.__arreglo[i] = self.__arreglo[i+1]
    def recorrer(self):
        for i in range(self.__cant):
            print(self.__arreglo[i])

    def elimiar(self,j=0):
        if j == self.__cant:
            print('A')
        else:
            for i in range(j,self.__cant,1):
               if self.__arreglo[j] == self.__arreglo[i+1]:
                   self.rshift(i+1)
                   self.__cant-=1
            j+=1
            self.elimiar(j)
    def insertarContenido(self,x):
        i = 0
        while x > self.__arreglo[i] and i < self.__cant:
            i+=1
        if not self.__arreglo[i] == x:
            self.shift(i)
            self.__arreglo[i] = x
            self.__cant += 1
