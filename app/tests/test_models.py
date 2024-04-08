import pytest
from app import app, db
from app.models.tasks import Tasks
from app.models.owner import Owner

@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app using the testing configuration
    with app.app_context():
        # Create all tables
        db.create_all()
        yield app.test_client()  # this is where the testing happens!
        db.drop_all()

def test_new_owner(test_client):
    """
    GIVEN a Owner model
    WHEN a new Owner is created
    THEN check the first_nm, last_nm, and email fields are defined correctly
    """
    owner = Owner(first_nm='John', last_nm='Doe', email='john.doe@example.com')
    db.session.add(owner)
    db.session.commit()
    assert owner.id is not None
    assert owner.first_nm == 'John'
    assert owner.last_nm == 'Doe'
    assert owner.email == 'john.doe@example.com'

def test_new_task(test_client):
    """
    GIVEN a Tasks model
    WHEN a new Task is created
    THEN check the task_name, task_priority, and task_owner fields are defined correctly
    """
    owner = Owner.query.first()
    task = Tasks(task_name='Test Task', task_priority=1, task_owner=owner.id)
    db.session.add(task)
    db.session.commit()
    assert task.id is not None
    assert task.task_name == 'Test Task'
    assert task.task_priority == 1
    assert task.task_owner == owner.id
