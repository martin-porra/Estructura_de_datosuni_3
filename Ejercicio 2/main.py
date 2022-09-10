from claseListaCursores import ListaCursores
if __name__ == '__main__':
    obj = ListaCursores()
    obj.insertar_contenido(10)
    obj.insertar_contenido(5)
    obj.insertar_contenido(20)
    print(obj.anterior(3))
    obj.supimir_contenido(20)
    obj.recorrer()



