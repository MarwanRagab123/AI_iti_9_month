USE ai46;

----------------------------------------
-- Query 1: List department managers 
-- (Manager first name + department name & number)
----------------------------------------
SELECT e.Fname, d.Dname, d.Dnum
FROM employee e, departments d
WHERE e.SSN = d.MGRSSN;

----------------------------------------
-- Query 2: List project names with their departments
----------------------------------------
SELECT d.Dname, p.Pname
FROM Project p, departments d
WHERE p.Dnum = d.Dnum;

----------------------------------------
-- Query 3: List dependents with their employee names
----------------------------------------
SELECT d.dependent_name, e.Fname
FROM dependent d, employee e
WHERE d.ESSN = e.SSN;

----------------------------------------
-- Query 4: Employees working >=10 hours 
-- on project 'Al Rabwah' AND department 10
----------------------------------------
SELECT e.Fname, p.Pname
FROM employee e 
INNER JOIN works_for w ON e.SSN = w.ESSn
INNER JOIN Project p ON p.Pnumber = w.Pno
WHERE w.Hours >= 10 
  AND p.Dnum = 10 
  AND p.Pname = 'Al Rabwah';

----------------------------------------
-- Query 5: Employees supervised by Kamel Mohamed
----------------------------------------
SELECT e.Fname
FROM employee e, employee s
WHERE e.Superssn = s.SSN 
  AND s.Fname = 'Kamel' 
  AND s.Lname = 'Mohamed';

----------------------------------------
-- Query 6: Managers who have no dependents
----------------------------------------
SELECT e.Lname
FROM employee e, departments s
WHERE s.MGRSSN = e.SSN 
  AND e.SSN NOT IN (SELECT ESSN FROM dependent);

----------------------------------------
-- Query 7: Department name of employee 
-- with minimum SSN in the company
----------------------------------------
SELECT s.Dname
FROM employee e, departments s
WHERE s.Dnum = e.Dno 
  AND e.SSN = (SELECT MIN(SSN) FROM employee);

----------------------------------------
-- Query 8: Salary statistics per department
----------------------------------------
SELECT d.Dname, 
       MAX(e.salary), 
       MIN(e.salary), 
       AVG(e.salary)
FROM employee e, departments d
WHERE d.Dnum = e.Dno
GROUP BY d.Dname;

----------------------------------------
-- Query 9: Departments where avg salary < 1200
----------------------------------------
SELECT d.Dname, d.Dnum, COUNT(e.SSN)
FROM employee e, departments d
WHERE d.Dnum = e.Dno
GROUP BY d.Dname, d.Dnum
HAVING AVG(e.salary) < 1200;

----------------------------------------
-- Query 10: Employees and their projects 
-- ordered by department, last name, first name
----------------------------------------
SELECT e.Fname, p.Pname
FROM employee e, works_for w, project p
WHERE w.Essn = e.SSN 
  AND w.Pno = p.Pnumber
ORDER BY e.Dno, e.Lname, e.Fname;

----------------------------------------
-- Query 11: Projects in Cairo city 
-- (project number, controlling dept, manager info)
----------------------------------------
SELECT 
    P.Pnumber,
    D.Dname AS Controlling_Department,
    E.Lname AS Manager_LastName,
    E.Address,
    E.Bdate
FROM project P
JOIN departments D ON P.Dnum = D.Dnum
JOIN employee E ON D.MGRSSN = E.SSN
WHERE P.City = 'Cairo';
