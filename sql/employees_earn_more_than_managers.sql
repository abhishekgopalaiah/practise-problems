--Employees who earn more than their managers

SELECT employee.*
FROM employees AS employee
JOIN employees AS manager 
     ON manager.EMPNO = employee.MGR 
WHERE employee.SAL > manager.SAL 
