# Simple Flask API

This project is intended to demonstrate a simple flask rest api applicaiton. It started out a way to take the time to understand flask app structure specific and has been developed into this.  My intention is to over time to continue to expand upon it with additional features as a learning tool.

## Scope

The application starts with two apis.  One for defining an owner and the second identifying their associated tasks. This project assumes that you have at the minimum an installation of python available to run the program.

## App structure
```
|-api/
|	|-app
|	|	|-__init__.py
|	|	|-extensions.py
|	|	|-models/
|	|	|	|-owner.py
|	|	|	|-tasks.py
|	|	|-owner/
|	|	|	|-__init__.py
|	|	|-tasks/
|	|	|	|-__init__.py
|	|	|-tests/
|	|	|	|-__init__.py
|	|	|	|-test_models.py
|	|	|	|-test_owner_api.py
|	|	|	|-test_tasks_api.py
|-config.py
|-requirements.py
```
## How to use

Since this application is intended to be simple, it is anticipated it will be run locally on your machine.  All instructions are geared towards a local installation and execution.

1. Create a directory on your local machine where you would like to run the application.  In my case, on windows, I am running it in my documents folder under a directory called api.
2. Next, change directories to the newly created folder and create a python virtual environment in the directory where it is intended to run the application:

```python -m venv .venv```

3. Activate the virtual environment:

```.venv/scripts/activate```

4. Check out the project to the directory where you intend to run the program.
5. Change directories to the location where you checked out the program.
6. Install all the package dependencies in the virtual machine:

```pip install -r requirements.txt```

This will install flask, flask_restful, flask_sqlalchemy, pytest, and Faker.

7. Now we can run the tests to make sure the application is working properly. Change directories to the tests directory:

```cd app/tests
./pytest test_models.py
./pytest test_owner_api.py
./pytest test_tasks_api.py
```

If all your tests passed, this has been successfully installed.  If you are receiving some kind of error, go back and make sure all the steps were followed properly. 

8. Start the application:

```flask --app app run```

9. Open a browser and go to the following url:

http://localhost:5000/owners  

While there is no data present, it will return a message showing that it attempted.

## Upcoming

* Documentation on how to access the remaining URLS
* Running the script to build fake owners and transactions to post to the api.
* Enhanced security on the apis.
whalla!

