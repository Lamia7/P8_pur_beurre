# P8: Pur Beurre
[Trello]()
Program only available in French now.

***How to use it***

### Context

### Installation and configuration 💻

**Clone the repository from Github by running this command:**

**Execute with a virtual environment:**
Create a virtual environment: `pipenv shell` <br>
_If you need to install pipenv : (with pip for Linux) `pip3 install pipenv` (with brew on Mac) `brew install pipenv` <br>
Activate the virtual environment: `source venv/bin/activate` <br>
_Install all the libraries through the requirements file: ... <br>_
Run the application: `python3 manage.py runserver` and go to your localhost : `http://127.0.0.1:8000/`

(To deactivate the virtual environment, run this command: ``)

### How does it work ?

### Features 📋
+ Authentication
+ (Research of a product and find a healthier substitute)
+ (Save substitutes)

### Checklist 📝
- [x] Download postgreSQL, added django + psycopg2 + libpq-dev
- [x] Initialize django project
- [x] Modify default settings
- [x] Create templates folder for templates organization
- [x] Create base.html template
- [x] Create the search app
- [x] Create home.html template
- [x] Create users app
- [x] Create register.html template/view + add to urls
- [x] Create auth.html template/view + add to urls
- [x] Create models for products, categories and favorites
- [x] Download data from OpenFoodFacts API
- [x] Create database and insert data into it

### Ressources used to create this program 🔧
***BACK***
- Language : Python 3.8
- Framework : Django
- Testing library : pytest
- HTTP library : requests
- Progression bar library : progress

***FRONT***
- Languages : Javascript, HTML5 & CSS3
- Frameworks : Bootstrap 4

***EXTERNAL RESSOURCES***
- Web server /  HTTP server : [Gunicorn](https://gunicorn.org/)

### Author 📝
[Lamia EL RALIMI](https://github.com/Lamia7)