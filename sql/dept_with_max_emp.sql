SELECT TOP 1 dept_name
FROM employees emp
JOIN departments dept
ON emp.dept_id = dept.dept_id
GROUP BY dept_name
ORDER BY COUNT(*) DESC