# Take-Your-Notes

### Requirements

* Python 3.8
* Postgresql
* Docker

### Setup
* Create .env file at the same level as manage.py file, and set variables: 

 SECRET_KEY,  DEBUG,  DB_NAME,  DB_USER,  DB_PASSWORD, DB_HOST

* Run command(for linux):
```bash
sudo docker-compose up --build
```
* Make necessary migrations:
```bash
docker-compose run web python manage.py migrate auth
docker-compose run web python manage.py migrate sessions
docker-compose run web python manage.py makemigrations note
docker-compose run web python manage.py makemigrations category
docker-compose run web python manage.py makemigrations user
docker-compose run web python manage.py migrate
```
* If you want to run the app use:
```bash
sudo docker-compose up
```
