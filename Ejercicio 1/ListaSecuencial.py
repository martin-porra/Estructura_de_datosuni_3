import numpy as np
class Lista:
 __lista : None
 __max = None
 __ul = None


 def __init__(self,max=10):
    self.__lista = np.empty(max,dtype=int)
    self.__max = max
    self.__ul = 0
 def insertar(self,p,x):
    if isinstance(x,int):
     if not self.lleno():
      if (p-1) >= 0 and (p-1)<= self.__ul+1:
       for i in range(self.__ul+1):
        if i == p-1:
            self.shift(i)
            self.__lista[i] = x
            self.__ul+=1
      else:
        print('Error: Posicion Invalida')
     else:
        print('Error: LIsta llena')

 def suprimir(self,p):
    if not self.vacia():
        if (p-1) >= 0 and (p-1)<= self.__ul:
         for i in range(self.__ul+1):
            if p-1 == i:
                self.rshift(i)
                self.__ul-=1

    else:
        print('Lista vacia')


 def lleno(self):
    return (self.__ul == self.__max-1)

 def vacia(self):
   return (self.__ul == 0)

 def shift(self,i):
    for j in range(self.__ul,i,-1):
        self.__lista[j] = self.__lista[j-1]

 def rshift(self,i):
    for j in range(i,self.__ul,1):
        self.__lista[j] = self.__lista[j+1]

 def recorrer(self):
    if not self.vacia():
        for i in range(self.__ul):
            print(self.__lista[i])
    else:
        print('Lista Vacia')

 def recuperar(self,p):
    if not self.vacia():
        if p-1 >= 0 and p-1 <= self.__ul:
            return self.__lista[p-1]
    else:
        print('Lista: Vacia')


 def insertarContenido(self,x):
     i=0
     while x > self.__lista[i] and i < self.__ul:
         i+=1
     self.shift(i)
     self.__lista[i] = x
     self.__ul+=1