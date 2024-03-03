from classroom.asignatura import Asignatura

class Grupo:
    grado = "12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        if asignaturas ==None:
            asignaturas=[]
        self._asignaturas= asignaturas
        if estudiantes ==None:
            estudiantes=[]
        self.listadoAlumnos = estudiantes
        
    def listadoAsignaturas(self,**kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))
    
    def agregarAlumno(self, alumno, lista=None):
        if lista ==None:
            lista=[]
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos+lista

    def __str__(self):
        cadena= "Grupo de estudiantes "+ self._grupo
        return cadena
    
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
