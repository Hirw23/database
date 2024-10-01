from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String(10), nullable=False)


DATABASE_URI = 'mysql+pymysql://walid:root@localhost/school_db'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#add student
def add_student(name, age, grade):
    new_student = Student(name=name, age=age, grade=grade)
    session.add(new_student)
    session.commit()
    print(f"Added student: {name}")

#read a recorde
def get_students_by_grade(grade):
    students = session.query(Student).filter_by(grade=grade).all()
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

#update function
def update_student_grade(student_id, new_grade):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.grade = new_grade
        session.commit()
        print(f"Updated student ID {student_id} to grade {new_grade}")
    else:
        print("Student not found")

#delete record

def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Deleted student ID {student_id}")
    else:
        print("Student not found")



# Example function calls (You can remove or modify these as needed)
add_student("John Doe", 16, "10th Grade")
get_students_by_grade("10th Grade")
update_student_grade(1, "11th Grade")
delete_student(1)
