from app import db
from app.extensions import reqparse, Resource
from app.models.owner import Owner

parser = reqparse.RequestParser()
parser.add_argument('first_nm', type=str, required=True, help='First Name is required')
parser.add_argument('last_nm', type=str, required=True, help='Last Name is required')
parser.add_argument('email', type=str, required=True, help='Email is required')

class OwnerResource(Resource):
    def get(self, owner_id):
        owner = db.session.get(Owner, owner_id)
        if owner:
            return {'first_nm': owner.first_nm, 'last_nm': owner.last_nm, 'email': owner.email}
        return {'message': 'Owner not found'}, 404

    def post(self, owner_id):
        args = parser.parse_args()
        owner = Owner(id=owner_id, first_nm=args['first_nm'], last_nm=args['last_nm'], email=args['email'])
        db.session.add(owner)
        db.session.commit()
        return {'message': 'Owner created successfully'}, 201
    
    def delete(self, owner_id):
        owner = db.session.get(Owner, owner_id)
        if owner:
            db.session.delete(owner)
            db.session.commit()
            return {'message': f'Owner {owner_id} deleted successfully'}
        return {'message': 'Task not found'}, 404
    
class AllOwners(Resource):
    def get(self):
        owners = Owner.query.all()
        owner_list = []
        for owner in owners:
            owner_list.append({'first_nm': owner.first_nm, 'last_nm': owner.last_nm, 'email': owner.email})
        return owner_list