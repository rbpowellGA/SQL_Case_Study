SELECT count(*)
FROM humanresources.employee
JOIN person.person USING(businessentityid)
JOIN person.emailaddress USING(businessentityid)
WHERE employee.vacationhours > 5
;