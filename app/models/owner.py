from app import db

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    first_nm = db.Column(db.String(100), nullable=False)
    last_nm = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)