Django project

1. Install, create and activate virtuval enviroment in project directory:
- pip install virtualvenv
- python -m venv ./venv
- .\venv\Scripts\activate

2. Install packages to virtual enviroment
- pip install -r requirements.txt

3. Run migrations and collect static
- python manage.py migrate
- python manage.py collectstatic

4. Runserver
- python manage.py runserver 

You can reach development server at http://127.0.0.1:8000/