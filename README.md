# Care24 - Content Management System
Care24 is a content management system built with Django and Django REST framework. It provides a set of RESTful API's to manage authors and their books.

## Installation

1. Clone the git repository or download the zip file and extract it in the project folder.

2. Create a virtual environment using the following command:
 ```
 python -m venv venv
```
3. Activate the virtual environment using the following command:
```
venv\Scripts\activate.bat
```
4. Install all packages using the following command or run next if first one gives errors:
```
pip install -r requirements.txt
```
```
pip install django djangorestframework drf-yasg django-filter PyJWT
```


## Usage
1. Seed admin users using this command: (Note: This cmd can create admin users, but it may also encounter errors. You can skip it and proceed to the next step.)
```
python manage.py seed authentication --number=2 --seeder "User.password" "David@932"
```
2. Run the server using the following command:
```
python manage.py runserver
```
3. Open the local server in your browser: (Swagger documentation is used to document the provided APIs.)
```
http://127.0.0.1:8000
```
4. For admin login, use the following credentials or create a new superuser: [email='dhawalp@gmail.com', password='David@932']
```
http://127.0.0.1:8000/admin
```
5. To begin, register a user. Then, log in to obtain a bearer token. (To log in, enter your email address and password.).
```
http://127.0.0.1:8000/register
http://127.0.0.1:8000/login
```
7. Next, use the bearer token to carry out CRUD operations. This includes creating, updating, partially updating, deleting, and searching for records using a query.
```
http://127.0.0.1:8000/api/author
http://127.0.0.1:8000/api/author/1
```
8. To perform a search, use the following URL:
```
http://127.0.0.1:8000/api/author?search=text
```


## License
Care24 is released under the MIT License. See LICENSE for more information.

## Credits
This project was built by Dhawal Patel.
