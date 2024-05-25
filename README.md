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
<strong>Validation</strong>Email Field set as EmailFeild which ensure the template of email id and unique constraint will ensure the existence of email id or not other fields required validation is also there.
