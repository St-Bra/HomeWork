import psycopg2

DB_CONFIG = {
    "dbname": "eschool_db",
    "user": "postgres",
    "password": "09890",
    "host": "localhost",
    "port": "5432"
}


def connect_db():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
   with connect_db() as conn, conn.cursor() as curr:
        curr.execute("""
            CREATE TABLE IF NOT EXIST courses(
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100) UNIQUE
            );
        """)

        curr.execute("""
            CREATE TABLE IF NOT EXIST students(
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100)
            );
        """)

        curr.execute("""
            CREATE TABLE IF NOT EXIST teachers(
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100) UNIQUE
            );
        """)

        curr.execute("""
            CREATE TABLE IF NOT EXIST grades(
            id SERIAL PRIMARY KEY,
            students_id INT REFERENCES students(id),
            courses_id INT REFERENCES courses(id),
            grade INT
            );
        """)

        