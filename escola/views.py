from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """ EXIBINDO TODOS OS ALUNES"""
    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """ EXIBINDO TODOS OS CURSOS """

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """ EXIBINDO TODAS AS MATRICULAS """

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer