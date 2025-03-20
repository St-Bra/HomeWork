CREATE DATABASE home_work

CREATE TABLE employees(
    id  SERIAL PRIMARY KEY,
    name VARCHAR(20),
    position VARCHAR(20),
    department VARCHAR(20),
    salary BIGINT
);


INSERT INTO employees (name, position, department, salary) VALUES
('Артём', 'FRONTEND', 'IT', 1800),
('Даниил', 'BACKEND', 'IT', 1900),
('Дмитрий', 'QA', 'IT', 1700),
('Егор', 'DevOps', 'IT', 2000);


UPDATE employees
SET position = 'Senior FRONTEND'
WHERE position = 'FRONTEND';

ALTER TABLE employees
ADD COLUMN "HireDate" VARCHAR;

UPDATE employees
SET "HireDate" = '20.06.2020';

UPDATE employees
SET position = 'Manager'
WHERE position = 'QA';


SELECT * FROM employees
WHERE position = 'Manager';

SELECT * FROM employees
WHERE salary > 500;

UPDATE employees
SET department = 'Sales'
WHERE position = 'DevOps';

SELECT * FROM employees
WHERE department = 'Sales';

SELECT ROUND(AVG(salary)) AS average_salary
FROM employees;

DROP TABLE employees;