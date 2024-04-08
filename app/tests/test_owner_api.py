import pytest
from flask import json
from app import app, db
from app.models.owner import Owner

@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert owner data
    owner1 = Owner(first_nm='John', last_nm='Doe', email='john.doe@example.com')
    db.session.add(owner1)
    db.session.commit()

    yield db  # this is where the testing happens!

    db.session.delete(owner1)
    db.session.commit()
    
def test_get_owner(test_client, init_database):
    response = test_client.get('/owner/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['first_nm'] == 'John'
    assert data['last_nm'] == 'Doe'
    assert data['email'] == 'john.doe@example.com'

def test_post_owner(test_client, init_database):
    response = test_client.post('/owner/100', json={
        'first_nm': 'Alice',
        'last_nm': 'Smith',
        'email': 'alice.smith@example.com'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'Owner created successfully'


def test_delete_owner(test_client, init_database):
    response = test_client.delete('/owner/100')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Owner 100 deleted successfully'

def test_get_all_owners(test_client, init_database):
    response = test_client.get('/owners/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['first_nm'] == 'John'
    assert data[0]['last_nm'] == 'Doe'
    assert data[0]['email'] == 'john.doe@example.com'

