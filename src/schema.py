import graphene
import graphene_sqlalchemy as gsql

from src import models


class Student(gsql.SQLAlchemyObjectType):

    class Meta:
        model = models.Student
        interfaces = (graphene.relay.Node, )


class Classe(gsql.SQLAlchemyObjectType):

    class Meta:
        model = models.Classe
        interfaces = (graphene.relay.Node, )


# class ClasseStudent(SQLAlchemyObjectType):
#
#     class Meta:
#         model = m.ass
#         interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    # all_S = gsql.SQLAlchemyConnectionField(Student)
    # all_c = gsql.SQLAlchemyConnectionField(Classe)

    student = graphene.relay.Node.Field(Student)
    classe = graphene.Field(Classe)

    students = graphene.List(Student)
    classes = graphene.List(Classe)

    # def resolve_student(self, info, id):
    #     query = Student.get_query(info).filter_by(id=id)
    #     return query.first()

    def resolve_students(self, info):
        query = Student.get_query(info)
        return query.all()

    def resolve_classes(self, info):
        query = Classe.get_query(info)
        return query.all()


schema = graphene.Schema(query=Query, types=[Student, Classe])
