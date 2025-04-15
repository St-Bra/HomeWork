from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

# Настройки базы данных
DB_URL = "postgresql://postgres:09890@localhost:5432/eschool_db"
engine = create_engine(DB_URL, echo=True)  # echo=True для вывода SQL-запросов
Session = sessionmaker(bind=engine)

Base = declarative_base()

# Модели
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(Text)

    enrollments = relationship('Enrollment', back_populates='course')

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, description={self.description})>"

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)

    enrollments = relationship('Enrollment', back_populates='student')

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    course_id = Column(Integer, ForeignKey('courses.id', ondelete='CASCADE'))
    grade = Column(Integer)

    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id}, grade={self.grade})>"

# Функция для инициализации базы данных (создание таблиц)
def init_db():
    Base.metadata.create_all(engine)

# --- Функции для работы с БД ---

def add_course(name, description):
    """Добавляет курс в базу данных"""
    session = Session()
    try:
        course = Course(name=name, description=description)
        session.add(course)
        session.commit()
        return course.id
    except IntegrityError:
        session.rollback()
        raise Exception(f"Курс с названием '{name}' уже существует.")
    finally:
        session.close()

def add_teacher(name, email):
    """Добавляет преподавателя в базу данных"""
    session = Session()
    try:
        teacher = Teacher(name=name, email=email)
        session.add(teacher)
        session.commit()
        return teacher.id
    except IntegrityError:
        session.rollback()
        raise Exception(f"Преподаватель с email '{email}' уже существует.")
    finally:
        session.close()

def add_student(name, email):
    """Добавляет студента в базу данных"""
    session = Session()
    try:
        student = Student(name=name, email=email)
        session.add(student)
        session.commit()
        return student.id
    except IntegrityError:
        session.rollback()
        raise Exception(f"Студент с email '{email}' уже существует.")
    finally:
        session.close()

def enroll_student(student_id, course_id, grade=None):
    """Оценивает студента в курсе"""
    session = Session()
    try:
        enrollment = Enrollment(student_id=student_id, course_id=course_id, grade=grade)
        session.add(enrollment)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise Exception("Ошибка при записи студента на курс.")
    finally:
        session.close()

def get_student_progress(student_id):
    """Получает прогресс студента (курсы и оценки)"""
    session = Session()
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            progress = []
            for enrollment in student.enrollments:
                progress.append((enrollment.course.name, enrollment.grade))
            return progress
        return None
    finally:
        session.close()

def search_course_by_name(name):
    """Ищет курсы по части названия"""
    session = Session()
    try:
        courses = session.query(Course).filter(Course.name.ilike(f"%{name}%")).all()
        return [(course.id, course.name, course.description) for course in courses]
    finally:
        session.close()
