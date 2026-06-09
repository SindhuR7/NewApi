from ..schemas.student_model import student

def create_admission(Student, db):
    new_student = student(**Student.dict())
    db.add(new_student)
    db.commit()
    db.refersh(new_student)
    return new_student

def get_students(db):
    return db.query(student).all()
 
