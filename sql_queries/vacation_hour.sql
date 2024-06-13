SELECT person.firstname, person.lastname, employee.jobtitle, emailaddress.emailaddress, employee.vacationhours
        FROM humanresources.employee
        JOIN person.person using(businessentityid)
        JOIN person.emailaddress using(businessentityid)
        WHERE employee.vacationhours > 40
         ;