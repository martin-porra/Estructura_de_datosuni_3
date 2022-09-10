import csv
from  Designacion import  designacion
from Lista import  Lista
if __name__ == '__main__':
    lista = Lista()
    archivo = open('estadistica.csv')
    reader = csv.reader(archivo,delimiter=',')
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            objet = designacion(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],)
            lista.insertar(objet)
    archivo.close()
    cargo = input('Ingresar cargo ')
    lista.cargo(cargo)
    año = input('Ingresar año ')
    cargo1 = input('Ingresar cargo ')
    materia = input('Ingresar materia ')
    lista.poraño(año,materia,cargo1)