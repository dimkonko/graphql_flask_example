import graphene

import graphene_sqlalchemy as gsql

import models as m


class Student(gsql.SQLAlchemyObjectType):

    class Meta:
        model = m.Student
        interfaces = (graphene.relay.Node, )


class Classe(gsql.SQLAlchemyObjectType):

    class Meta:
        model = m.Classe
        interfaces = (graphene.relay.Node, )


# class ClasseStudent(SQLAlchemyObjectType):
#
#     class Meta:
#         model = m.ass
#         interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    # all_S = gsql.SQLAlchemyConnectionField(Student)
    # all_c = gsql.SQLAlchemyConnectionField(Classe)

    student = graphene.Field(Student)
    classe = graphene.Field(Classe)

    students = graphene.List(Student)
    classes = graphene.List(Classe)

    def resolve_students(self, info):
        query = Student.get_query(info)
        return query.all()

    def resolve_classes(self, info):
        query = Classe.get_query(info)
        return query.all()


schema = graphene.Schema(query=Query)

# schema.execute('''
# {
# classes
# }
# ''')
