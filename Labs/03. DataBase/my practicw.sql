use ai46;


select  d.Dnum,d.Dname,e.SSN,e.Fname
from employee e ,departments d
where d.MGRSSN=e.SSN;

select d.Dname,p.Pname
from departments d,Project p
where p.Dnum=d.Dnum;

select d.dependent_name,e.Fname
from dependent d, employee e
where e.SSN=d.ESSN;

select e.Fname,Pname
from employee e inner join works_for w
	on e.SSN=w.ESSN
    inner join project p
    on p.Pnumber=w.Pno
    where e.Dno=10 and Hours>=10 and Pname='Al Rabwah';
    

select e.Fname
from employee e ,employee r
where e.Superssn=r.SSN  and  r.Fname="Kamel" and r.Lname="Mohamed";

select e.Lname
from employee e left outer join dependent t
	on e.SSN=t.ESSN
    inner join departments
    on MGRSSN=e.SSN and t.dependent_name is null;
    

select d.Dname
from employee e,departments d
where d.Dnum = e.Dno and e.SSN= (select min(SSN) from employee);


select d.Dname, max(e.salary) as Max_Salary, min(e.salary) as Min_Salary,avg(e.salary)as Average_Salary
from employee e , departments d
where d.Dnum = e.Dno
group by d.Dname;
    
select d.Dname , d.Dnum ,e.SSN , e.salary
from employee e , departments d
where d.Dnum = e.Dno
group by d.Dnum , e.SSN
having avg(e.salary<1200);

select e.Fname ,p.Pname
from departments d inner join project p
	on d.Dnum=p.Dnum
    inner join employee e
	on e.Dno=d.Dnum
    order by e.Dno ,e.Fname,e.Lname;
    

SELECT  e.fname, p.pname 
FROM works_for AS w, employee AS e, project AS p 
WHERE w.essn=e.ssn  
and w.pno=p.pnumber 
ORDER BY e.dno, e.lname, e.fname; 


select p.Pnumber ,d.Dname,e.Lname,e.Address,e.Bdate,p.city
from departments d inner join project p
	on d.Dnum=p.Dnum
    inner join employee e
	on e.SSN=d.MGRSSN and p.city='cairo';
  

