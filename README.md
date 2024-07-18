## Getting Started
To get a copy of the project up and running on your local machine for development and testing purposes,

1. **clone** this repository 
   ```sh
   git clone https://github.com/KarenNgala/TC4A.git

   cd TC4A
   ```
2. Install and actvate a virtual environment
   ```sh
   $ python3 -m venv virtual

   $ source virtual/bin/activate
   ```

3. Install **pip** and project **dependencies**
   ```sh
   (virtual) $ pip install -r requirements.txt
    ```

### Database requirements
1.  To get a development env running, use the **.env.example** file to create **your own** `.env` file.
```sh
cp .env.example .env

# Update .env with your PostgreSQL settings
```
* Generate a new secret key using [Djecrety](https://djecrety.ir/) to quickly generate secure secret keys.
2.  Create a **postgres** db and add the credentials to the .env file
```sh
psql
CREATE DATABASE <db-name>
```
3.  Apply migrations to create database schema
```sh 
(virtual) $ python manage.py makemigrations

(virtual) $ python manage.py migrate
```
4.  Run server
```sh
 (virtual) $ python3 manage.py runserver
 ```

## Running the tests
To run automated tests for this system:
```sh
(virtual) $ python3 manage.py test application
```
The API will be available at http://127.0.0.1:8000/application/.


## Built With

* Django
* Django REST Framework
* PostgreSQL

## License
This project is licensed under the MIT License - see the LICENSE.md file for details