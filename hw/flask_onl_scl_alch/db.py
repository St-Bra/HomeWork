from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, CheckConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Создаём базовый класс для всех моделей
Base = declarative_base()

# URL для подключения к базе данных
DATABASE_URL = "postgresql://postgres:09890@localhost:5432/eschool_db"

# Создаём движок для подключения к БД
engine = create_engine(DATABASE_URL)

# Создаём сессию для работы с БД
Session = sessionmaker(bind=engine)

# Определяем модели для таблиц

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True)
    description = Column(Text)
    deleted_at = Column(DateTime, default=None)

    enrollments = relationship('Enrollment', back_populates='course')


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    deleted_at = Column(DateTime, default=None)

    enrollments = relationship('Enrollment', back_populates='student')


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    deleted_at = Column(DateTime, default=None)


class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    course_id = Column(Integer, ForeignKey('courses.id', ondelete='CASCADE'))
    grade = Column(Integer, CheckConstraint('grade BETWEEN 0 AND 100'))
    deleted_at = Column(DateTime, default=None)

    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')


# Создание таблиц в базе данных
def init_db():
    Base.metadata.create_all(engine)

# Функции для работы с БД

def add_course(name, description):
    """Добавляет курс"""
    session = Session()
    course = Course(name=name, description=description)
    session.add(course)
    session.commit()
    session.refresh(course)
    session.close()
    return course.id

def del_course(course_id):
    """Удаляет курс"""
    session = Session()
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        course.deleted_at = datetime.utcnow()
        session.commit()
    session.close()

def edit_course(course_id, new_name, new_description):
    """Редактирует курс"""
    session = Session()
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        course.name = new_name
        course.description = new_description
        session.commit()
    session.close()
    return course.id

def get_all_courses():
    """Получает все курсы"""
    session = Session()
    courses = session.query(Course).filter(Course.deleted_at == None).all()
    session.close()
    return [(course.name, course.description, course.id) for course in courses]

def add_teacher(name, email):
    """Добавляет преподавателя"""
    session = Session()
    teacher = Teacher(name=name, email=email)
    session.add(teacher)
    session.commit()
    session.refresh(teacher)
    session.close()
    return teacher.id

def del_teacher(teacher_id):
    """Удаляет преподавателя"""
    session = Session()
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
    session.close()

def edit_teacher(teacher_id, new_name, new_email):
    """Редактирует преподавателя"""
    session = Session()
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        teacher.name = new_name
        teacher.email = new_email
        session.commit()
    session.close()
    return teacher.id

def get_all_teachers():
    """Получает всех преподавателей"""
    session = Session()
    teachers = session.query(Teacher).all()
    session.close()
    return [(teacher.id, teacher.name, teacher.email) for teacher in teachers]

def add_student(name, email):
    """Добавляет студента"""
    session = Session()
    student = Student(name=name, email=email)
    session.add(student)
    session.commit()
    session.refresh(student)
    session.close()
    return student.id

def del_student(student_id):
    """Удаляет студента"""
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
    session.close()

def edit_student(student_id, new_name, new_email):
    """Редактирует студента"""
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = new_name
        student.email = new_email
        session.commit()
    session.close()
    return student.id

def get_all_students():
    """Получает всех студентов"""
    session = Session()
    students = session.query(Student).all()
    session.close()
    return [(student.id, student.name, student.email) for student in students]

def enroll_student(student_id, course_id, grade=None):
    """Оценивает студента"""
    session = Session()
    enrollment = Enrollment(student_id=student_id, course_id=course_id, grade=grade)
    session.add(enrollment)
    session.commit()
    session.close()

def get_student_progress(student_id):
    """Получает успеваемость студента"""
    session = Session()
    progress = session.query(Course.name, Enrollment.grade).join(Enrollment).filter(Enrollment.student_id == student_id).all()
    session.close()
    return progress

def search_course_by_name(name):
    """Ищет курс по имени"""
    session = Session()
    courses = session.query(Course).filter(Course.name.ilike(f"%{name}%")).all()
    session.close()
    return [(course.id, course.name, course.description) for course in courses]
