#Una clase en Python es una estructura que permite definir objetos con atributos y métodos relacionados. Las clases sirven como plantillas para crear instancias, que son objetos específicos basados en la definición de la clase. Las clases en Python son una forma de implementar la programación orientada a objetos.

#ejercicio#1- definicion de una class

# class persona:
#     def __init__(self,nombre,edad):
#         #metodo especial para inicializar los objetos
#         self.nombre=nombre
#         self.edad=edad
# #creacion de un objeto de la clase persona 
# persona1=persona("camilo",25)
# #acceder a los atributos del objeto 
# print(persona1.nombre)
# print(persona1.edad)

# #ejercicio#2-por herencia

# class estudiante(persona):
#     def __init__ (self, nombre,edad,universidad):
#         #se llama a la clase padre
#         super().__init__(nombre,edad)
#         self.universidad=universidad
# #creacion de un objeto 
# estudiante1=estudiante("Ana",22,"UNAD")
# #acceder a los atributos
# print(estudiante1.nombre)
# print(estudiante1.edad)
# print(estudiante1.universidad)

#ejercicio#3 

# class coches:
#     cantidadCoches=0#atributo de clase para contar la cantidad de objetos
# def __init__ (self,modelo):
#     self.modelo=modelo
#     coches.cantidadCoches+=1 #incrementar la cantidad de coches al crear uno
# #uso del atributo de clase
# coche1=coches("sedan")
# cache2=coches("suv")
# print(coches.cantidadCoches)#imprimira los dos objetos de la clase coches

#ejercicio#4

# class persona:
#     def __init__(self,nombre,edad):
#         #construir la inicializacion del objeto persona
#         self.nombre=nombre
#         self.edad=edad

#         def obtenerInfo(self):
#             #metodo que imprime la informacion del objeto persona
#             print("nombre: {sefl.nombre}, edad: {sefl.edad}")

#             class estudiante(persona):
#                 def __init__(self,nombre,edad,curso):
#                     #constructor que inicializa el objeto estudiante con nombre,edad y curso 
#                     super().__init__(nombre,edad)
#                     self.curso=curso

#                     def obtenerInfo(self):
#                         #la informacion del estudiante
#                         print("nombre: {sefl.nombre}, edad: {self.edad}, curso: {self.curso}")
# persona1= persona("juan",25)
# #mostrar la informacion del objeto persona
# persona1.obtenerInfo()

# estudiante1=("maria",20,"python")
# #mostrar la informacion del objeto estudiante 
# estudiante1.obtenerInfo()