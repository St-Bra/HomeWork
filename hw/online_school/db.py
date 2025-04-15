import psycopg2

DB_CONFIG = {
    "dbname": "eschool_db",
    "user": "postgres",
    "password": "09890",
    "host": "localhost",
    "port": "5432"
}

def connect_db():
    """Создаёт и возвращает соединение с БД"""
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    """Создаёт таблицы, если их нет"""
    with connect_db() as conn, conn.cursor() as curr:
        # Создание таблиц
        curr.execute("""
            CREATE TABLE IF NOT EXISTS courses(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) UNIQUE,
                description TEXT,
                deleted_at TIMESTAMP DEFAULT NULL
            );
        """)

        curr.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE,
                deleted_at TIMESTAMP DEFAULT NULL
            );
        """)

        curr.execute("""
            CREATE TABLE IF NOT EXISTS teachers(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE,
                deleted_at TIMESTAMP DEFAULT NULL
            );
        """)

        curr.execute("""
            CREATE TABLE IF NOT EXISTS enrollments(
                id SERIAL PRIMARY KEY,
                student_id INT REFERENCES students(id) ON DELETE CASCADE,
                course_id INT REFERENCES courses(id) ON DELETE CASCADE,
                grade INT CHECK (grade BETWEEN 0 AND 100),
                deleted_at TIMESTAMP DEFAULT NULL
            );
        """)

        conn.commit()

# --- Функции для работы с БД ---

def add_course(name, description):
    """Добавляет курс"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("INSERT INTO courses (name, description) VALUES (%s, %s) RETURNING id;", (name, description))
        conn.commit()
        return curr.fetchone()[0]

def del_course(course_id):
    """Удаляет курс"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("UPDATE courses SET deleted_at = CURRENT_TIMESTAMP WHERE id = %s;",(course_id,))

def edit_course(course_id, new_name, new_description):
    """Редактирует курс"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("""
            UPDATE courses 
            SET name = %s, description = %s 
            WHERE id = %s RETURNING id;
        """, (new_name, new_description, course_id))
        conn.commit()
        return curr.fetchone()[0]

def get_all_courses():
    """Получает все курсы"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("SELECT name, description FROM courses WHERE deleted_at IS NULL;")
        return curr.fetchall()

def add_teacher(name, email):
    """Добавляет преподавателя"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("INSERT INTO teachers (name, email) VALUES (%s, %s) RETURNING id;", (name, email))
        conn.commit()
        return curr.fetchone()[0]

def del_teacher(teacher_id):
    """Удаляет преподавателя"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("DELETE FROM teachers WHERE id = %s RETURNING id;", (teacher_id,))
        conn.commit()
        return curr.fetchone()[0]

def edit_teacher(teacher_id, new_name, new_email):
    """Редактирует преподавателя"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("""
            UPDATE teachers 
            SET name = %s, email = %s 
            WHERE id = %s RETURNING id;
        """, (new_name, new_email, teacher_id))
        conn.commit()
        return curr.fetchone()[0]

def get_all_teachers():
    """Получает всех преподавателей"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("SELECT * FROM teachers;")
        return curr.fetchall()

def add_student(name, email):
    """Добавляет студента"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("INSERT INTO students (name, email) VALUES (%s, %s) RETURNING id;", (name, email))
        conn.commit()
        return curr.fetchone()[0]

def del_student(student_id):
    """Удаляет студента"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("DELETE FROM students WHERE id = %s RETURNING id;", (student_id,))
        conn.commit()
        return curr.fetchone()[0]

def edit_student(student_id, new_name, new_email):
    """Редактирует студента"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("""
            UPDATE students 
            SET name = %s, email = %s 
            WHERE id = %s RETURNING id;
        """, (new_name, new_email, student_id))
        conn.commit()
        return curr.fetchone()[0]

def get_all_students():
    """Получает всех студентов"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("SELECT * FROM students;")
        return curr.fetchall()

def enroll_student(student_id, course_id, grade=None):
    """Оценивает студента"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("INSERT INTO enrollments (student_id, course_id, grade) VALUES (%s, %s, %s);",
                     (student_id, course_id, grade))
        conn.commit()

def get_student_progress(student_id):
    """Получает успеваемость студента"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("""
            SELECT c.name, e.grade 
            FROM enrollments e
            JOIN courses c ON e.course_id = c.id
            WHERE e.student_id = %s;
        """, (student_id,))
        return curr.fetchall()

def search_course_by_name(name):
    """Ищет курс по имени"""
    with connect_db() as conn, conn.cursor() as curr:
        curr.execute("SELECT id, name, description FROM courses WHERE name ILIKE %s;", (f"%{name}%",))
        return curr.fetchall()
