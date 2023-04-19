# Care24 - content_management_system

Clone the git repository or download zipfile and extract in the project folder.

Create Virtual Environment using cmd "python -m venv venv"

Active Environment using cmd "venv\Scripts\activate.bat"

Install all packages using cmd "pip install -r requirements.txt"

Admin Users are seeded using this cmd it create users but it gives error option it run directly using below cmd (python manage.py seed authentication --number=2 --seeder "User.password" "David@932")

Run Server using cmd "python manage.py runserver"

Open local Server in Browser "http://127.0.0.1:8000" swagger documentation provided. (admin credentitals [username='dhawalp', password='David@932'])

First Register User after registration Login to get bearer token ( Login using username, Registerations extra fields can be add from admin )

Then use bearer token to login and you can create, update, partial update, delete, search using query to get searched record.
