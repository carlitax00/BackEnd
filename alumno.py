class Alumno:
    def __init__ (self, nombre, apellido, edad, curso): # este es un método
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso

    def __del__ (self):  # __del__ garantiza que todo lo que se haya construido en ese momento, cuando ese objeto deje de ser referenciado, se destruya (por ej, una conexión
        pass             # a una base de datos, si no se cerró en el objeto)
      # pass permite no implemetar el método, o sea que no haga nada

    def __str__ (self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.curso}"

ObjectAlumno = Alumno("Juan", "Perez", 20, "Python")  # acá se está construyendo el objeto, llamando al método de la clase Alumno

print(ObjectAlumno.nombre)

print(ObjectAlumno) # si tiene __str__ se imprime el resultado del método