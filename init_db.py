from src.database import engine, db_session
from src.models import Base, Student, Classe

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Create the fixtures

# Students
ron = Student(name='Ron')
harry = Student(name='Harry')
herm = Student(name='Hermiona')
db_session.add_all([ron, harry, herm])

# Classes
c1 = Classe(name='Magic')
c2 = Classe(name='Math')

# cs1 = ClasseStudent(student=ron)
# cs2 = ClasseStudent(student=harry)
# c1.students.extend([cs1, cs2])
#
# cs3 = ClasseStudent(student=herm)
# c2.students.extend([cs3])

c1.students.extend([ron, harry])
c2.students.extend([herm])

db_session.add_all([c1, c2])

db_session.commit()
