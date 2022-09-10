import  csv
from Lista import  Lista
if __name__ == '__main__':
    lista = Lista()
    archivo = open('superficie.csv')
    reader = csv.reader(archivo, delimiter=(';'))
    band = True
    x = 0
    band2 = True
    cantidad = 0.0
    nombre = ''
    for fila in reader:
        if band:
            band = False
        else:
            a = fila[2]
            if x == fila[2]:
                if fila[6] != '':
                 num = fila[6]
                 cantidad =float(num)+float(cantidad)
                 nombre = fila[3]
            else:
                if band2:
                  band2 = False
                  x = a
                  cantidad = fila[6]
                  nombre = fila[3]
                else:
                 x = a
                 lista.insertar(cantidad,nombre)
                 if fila[6] != '':
                  cantidad = float(fila[6])
                  nombre = fila[3]
    archivo.close()
    lista.recorrer()


