<h1>Django Employee Management Application</h1>
<strong>Flow of the Task: </strong><br>
<strong>"employees"</strong> is the project name and <strong>"employee_mgmt"</strong> folder is the django application name<br><br>
<strong>A. models.py</strong>: comprises two models <strong>"Employee"</strong> and <strong>"Skill"</strong> and Employee has many to many relationship with skills.<br></p>
<strong>B. serializers.py</strong>:  comprise two serilaizers classes : 4.1 - SkillSerializer for Skill model and 4.2 - EmployeeSerializer dor Employee Model, consitrutor override to display the all the saved skill data in the POST Form and SkillSerilaizer class for getting the all related data<br><br>
<strong>C. views,py: </strong>used ModelViewsets for default CRUD operations<br><br>
<strong>D. urls.py :</strong> Defaulterroyter used for rAPI endpoint Creation<br><br>
<strong>E. admins.py:</strong> Registering the Two models and auto-suggestion of Skills in Employe table. by using autocomplete_fields in SkillAdmin Class and overriding the get_search_results in EmployeeAdmin class<br><br>
<ul>API Endpoints:
<li>1. List all employees: http://127.0.0.1:8000/api/employees/</li>
<li>2. Retrieve a single employee.: http://127.0.0.1:8000/api/employees/<id>/</li>
<li>3. Create a new employee.: http://127.0.0.1:8000/api/employees/</li>
<li>4. Update an existing employee.: http://127.0.0.1:8000/api/employees/<id>/</li>
<li>5. Delete an employee.:http://127.0.0.1:8000/api/employees/<id>/</li>
<li>6. List all skills.: http://127.0.0.1:8000/api/skill/</li>
<li>7. Retrieve a single skill.: http://127.0.0.1:8000/api/skill/<id>/</li>
<li>8. Create a new skill.:http://127.0.0.1:8000/api/skill/</li>
<li>9. Update an existing skill.: http://127.0.0.1:8000/api/skill/<id>/</li>
<li>10. Delete a skill.: http://127.0.0.1:8000/api/skill/<id>/</li><br><br>
<strong>Validation</strong>Email Field set as EmailFeild which ensure the template of email id and unique constraint will ensure the existence of email id or not other fields required validation is also there.<br>
<h3>Frontend Implementation:</h3>
1. <strong>forms.py</strong>: forms for skill table and employee table created and for validation of first name and last name<br>
2. <strong>Django Templates</strong>: created two templates (one is success.html: this is the Home Page) and (other template is employee-form.html for rendering the add form, update form)<br>
3. <strong>views.py</strong>: created add employee view, update employee view and delete employee view and one for skill auto-suggestion view<br>
4. <strong>skill auto-suggestion: </strong> in the "employee-form.html" there is one javascript code which will fetch the auto-suggestion view based on the partials matches in the skill field and also handled the comma separted skills added by the user in skill field and auto-suggestion for comma seprated skills.<br>
5. <strong>Validation</strong>:<br> 5.1. First name and last name validation, which should only accept the alphabets not number and special character <br>5.2. Email id already exist validation using Unique constrint in models.py corspoinding to the email field and also ensure the email format, <br>5.3. Also handled the unique ness of skills when creating, in the views.py i am checking at the time of adding the new skills.<br>
6. <strong>Javascript auto-suggestion:</strong> checks if skills typed in the skill field exists or not, if not then letting user to add the new one and if exists then asking them to select the existing skills only. in the views.py auto-suggestion handled by taking the skill field value <br>
7.<strong>urls.py</strong> urls for a. home page: http://127.0.0.1:8000/welcome/<br>b. add new employee: http://127.0.0.1:8000/employee-form/<br>c. update the employee deatils: http://127.0.0.1:8000/employee-data-update/7/<br>d.http://127.0.0.1:8000/emp-delete/8/<br>
8. <strong>Views.py</strong>:add new employee: employee_view, update employee: emp_update, delete employee: emp_delete, for home page: welcome.view, for auto-suggestion:skill_suggestion.
