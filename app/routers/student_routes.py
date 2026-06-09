from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.student_model import CreateStudent
from ..config.database import get_db
from ..controllers.student_controller import create_admission, get_students

studentRouter = APIRouter()

@studentRouter.post('/students_admissions')
def create(student: CreateStudent, db:Session = Depends(get_db)):
    return create_admission(student, db)

@studentRouter.get('/all_students')
def get(db:Session=Depends(get_db)):
    return get_students(db)