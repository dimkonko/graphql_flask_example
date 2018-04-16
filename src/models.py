from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Table, outerjoin
from sqlalchemy.orm import backref, relationship

from src.database import Base


ass = Table(
    'classe_student', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('classe_id', Integer, ForeignKey('classe.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
)


# class ClasseStudent(Base):
#     __tablename__ = 'classe_student'
#     id = Column(Integer, primary_key=True)
#     classe_id = Column(Integer, ForeignKey('classe.id'))
#     student_id = Column(Integer, ForeignKey('student.id'))
#
#     student = relationship('Student', back_populates='classes')
#     classe = relationship('Classe', back_populates='students')


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # classes = relationship('ClasseStudent')
    classes = relationship('Classe',
                           secondary=ass,
                           # secondaryjoin=id == ass.c.student_id
                           lazy='subquery'
                           )
    # results = relationship('Result', lazy='joined')


class Classe(Base):
    __tablename__ = 'classe'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # students = relationship('ClasseStudent', lazy='joined')
    students = relationship('Student',
                            secondary=ass,
                            # secondaryjoin=id == ass.c.classe_id,
                            lazy='subquery'
                            )


# class Result(Base):
#     __tablename__ = 'result'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     mark = Column(Integer)
