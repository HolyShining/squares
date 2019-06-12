# Startup project:

## `Via Docker:`
1. Clone project from GitHub
2. Add `.env` file from attachment with secret key to root folder
3. Run in terminal: `docker-compose up`
4. Go to the `localhost:8000`

## `Via OS:`
1. Clone project from GitHub
2. Add secret key from attachment to `sftp_client/settings.py` at line `11` \
   or add secret key to enviroment variables in system
3. Install Pipenv:
	* For Mac: `brew install pipenv`
	* For Linux: `apt install -y pipenv`
	* For Windows: `pip install pipenv`

4. Run `pipenv install` at root folder to install project dependencies
5. Migrate the database via `pipenv python manage.py migrate`
6. Run `pipenv run python manage.py runserver` to start Django project
7. Go to the `localhost:8000`
