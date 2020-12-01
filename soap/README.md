# SOAP

1. **Assignment 4 - SOAP and WSDL.docx** 
- contains the project's/Assignment's deliverables.

2. **soap** 
- django project that contains an app called *soap_students_app*, which implements the soap web service.
- the django project is configured to use a mysql database.
- to add students into the db, a ui is provided by accessing http://127.0.0.1:8000/admin/ Image included below.
- need to ensure the server is running, *python manage.py runserver*
- you can then proceed to running *soap_students_client.py*, explained below.
- to access the WSDL, visit http://127.0.0.1:8000/soap_service/?WSDL

3. **soap_students_client.py** 
- client that consumes the soap web service. 
- Need to pass in the student's admission number in order to get his/her details.
- run as follows: *python soap_students_client.py*


**resources** - contains random pieces of information consulted in order to implement the project. Useful for future reference.

**Requirements:**
Project was done in a virtual environment using python 2.7, the following should help:
*resources/python_versions*
*resources/virtual_environments*
*resources/mysql-server and django*
pip install Django==1.8
pip installSpyne==2.10
pip install Suds==0.4
pip install lxml

Interface for storing student's details into a mysql database:
![register_students_ui](https://github.com/aubreyomondi/distributed_objects_labs/blob/main/soap/images/register_students_ui.png)



