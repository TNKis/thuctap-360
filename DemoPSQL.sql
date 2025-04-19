CREATE DATABASE company_db;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50)
);

INSERT INTO employees (name, age, department) VALUES ('Nguyễn Văn A', 28, 'Marketing');
INSERT INTO employees (name, age, department) VALUES ('Trần Văn B', 35, 'Sales');
INSERT INTO employees (name, age, department) VALUES ('Lê Thị C', 40, 'HR');

SELECT * FROM employees;

SELECT name, age FROM employees WHERE age > 30;

INSERT INTO employees (name, age, department) VALUES ('Nguyễn Văn A', 28, 'Marketing');

UPDATE employees SET age = 29 WHERE name = 'Nguyễn Văn A';

UPDATE employees SET department = 'Sales' WHERE department = 'Marketing';