from app import db

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    task_priority = db.Column(db.Integer, nullable=False)
    task_owner = db.Column(db.Integer, db.ForeignKey('owner.id'))

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    first_nm = db.Column(db.String(100), nullable=False)
    last_nm = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)