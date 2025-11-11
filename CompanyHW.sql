SELECT * FROM employees WHERE dept = 'IT';

SELECT * FROM employees WHERE salary > 70000;

SELECT * FROM employees WHERE exp BETWEEN 3 AND 6;

SELECT * FROM employees WHERE dept = 'HR' OR dept = 'Sales';

SELECT * FROM employees ORDER BY salary DESC LIMIT 3 ;

SELECT name, dept, MIN(salary) FROM employees GROUP BY dept;

SELECT * FROM employees ORDER BY exp DESC; 

SELECT AVG(salary) AS Average_Salary FROM employees;

SELECT * FROM employees WHERE name LIKE "s%";

SELECT * FROM employees WHERE salary > 60000 AND dept = 'sales';