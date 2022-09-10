class designacion:
 __año = None
 __justifica = None
 __cargo = None
 __instancia = None
 __materia = None
 __cantidadv = None
 __cantidadm = None

 def __init__(self,año,justificacion,cargo,instancia,materia,varon,mujer):
  self.__año = año
  self.__justifica = justificacion
  self.__cargo = cargo
  self.__instancia = instancia
  self.__materia = materia
  self.__cantidadv = varon
  self.__cantidadm = mujer

 def getaño(self):
  return self.__año
 def getcargo(self):
  return self.__cargo
 def getm(self):
  return self.__cantidadm
 def getv(self):
  return self.__cantidadv
 def getmateria(self):
  return self.__materia