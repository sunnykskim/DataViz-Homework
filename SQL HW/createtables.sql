CREATE TABLE departments (
  dept_no varchar NOT NULL,
  dept_name varchar NOT NULL
);

CREATE TABLE dept_emp (
emp_no varchar NOT NULL,
dept_no	varchar NOT NULL,
from_date date,
to_date date
);

CREATE TABLE dept_manager (
dept_no varchar NOT NULL,
emp_no varchar NOT NULL,
from_date date,
to_date date
);

CREATE TABLE employees (
emp_no varchar NOT NULL,
birth_date date,
first_name varchar NOT NULL,
last_name varchar NOT NULL,
gender varchar NOT NULL,
hire_date date
);

CREATE TABLE salaries (
emp_no varchar NOT NULL,
salary int,
from_date date,
to_date date
);

CREATE TABLE titles (
emp_no varchar NOT NULL,
title varchar NOT NULL,
from_date date,
to_date date
);
