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

    # Create the database and the database table
    db.create_all()
    
    owner1 = Owner(first_nm='John', last_nm='Doe', email='john.doe@example.com')
    db.session.add(owner1)
    db.session.commit()

    yield testing_client  # this is where the testing happens!

    # Teardown: drop all tables and remove context
    db.session.remove()
    db.session.delete(owner1)
    db.session.commit()
    ctx.pop()

def test_post_task(test_client):
    # Post a new task
    response = test_client.post('/tasks/1', json={
        'task_name': 'New Task',
        'task_priority': 5,
        'task_owner': 1  # Assuming there is an owner with id 1
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'Task created successfully'

def test_get_task(test_client):
    # Assuming there is a task with id 1
    response = test_client.get('/tasks/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['task_id'] == 1
    assert 'task_name' in data
    assert 'task_priority' in data

def test_post_task(test_client):
    # Post a new task
    response = test_client.post('/tasks/1', json={
        'task_name': 'New Task',
        'task_priority': 5,
        'task_owner': 1  # Assuming there is an owner with id 1
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'Task created successfully'

def test_get_all_tasks(test_client):
    # Get all tasks
    response = test_client.get('/tasks/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    # Check that each task has the required fields
    for task in data:
        assert 'task_id' in task
        assert 'task_name' in task
        assert 'task_priority' in task

def test_delete_task(test_client):
    # Delete the task with id 1
    response = test_client.delete('/tasks/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Task deleted successfully'
