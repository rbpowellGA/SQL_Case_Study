SELECT CONCAT(person.firstname,' ',person.lastname) AS name
     , employee.jobtitle, emailaddress.emailaddress  AS "email address"
     , employee.vacationhours AS "40+ VacationHours"
FROM humanresources.employee
JOIN person.person USING(businessentityid)
JOIN person.emailaddress USING(businessentityid)
WHERE employee.vacationhours > 40
         ;