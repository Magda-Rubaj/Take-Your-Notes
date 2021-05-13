# Take-Your-Notes

### Requirements

* Python 3.8
* Postgresql
* Docker

### Setup
* Create and configure postgresql database
* Create .env file at the same level as manage.py file, and set variables: 

 SECRET_KEY,  DEBUG,  DB_NAME,  DB_USER,  DB_PASSWORD, DB_HOST

* Run command(for linux):
```bash
sudo docker-compose up
```
* If you want to run the app make sure your database is up and use either:
```bash
sudo docker-compose up
```
or 
```bash
sudo docker-compose run web python manage.py runserver
```
