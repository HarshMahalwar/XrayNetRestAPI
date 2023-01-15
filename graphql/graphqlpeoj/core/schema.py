import graphene
from graphene_django import DjangoObjectType
from .models import Employee


class EmployeeTable(DjangoObjectType):
    class Meta:
        model = Employee
        fields = ('name', 'age')


class Query(graphene.ObjectType):
    employees = graphene.List(EmployeeTable)

    def resolve_employees(root, info):
        return Employee.objects.all()


schema = graphene.Schema(query=Query)