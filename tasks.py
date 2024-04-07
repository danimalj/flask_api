from app import db
from extensions import reqparse, Resource
from models import Tasks

parser = reqparse.RequestParser()
parser.add_argument('task_name', type=str, required=True, help='Task name is required')
parser.add_argument('task_priority', type=int, required=True, help='Task priority is required')
parser.add_argument('task_owner', type=int, required=False, help='Task owner is required')

class TaskResource(Resource):
    def get(self, task_id):
        task = Tasks.query.get(task_id)
        if task:
            return {'task_id': task.id, 'task_name': task.task_name, 'task_priority': task.task_priority, 'task_owner': task.task_owner}
        return {'message': 'Task not found'}, 404

    def post(self, task_id):
        args = parser.parse_args()
        task = Tasks(id=task_id, task_name=args['task_name'], task_priority=args['task_priority'], task_owner=args['task_owner'])
        db.session.add(task)
        db.session.commit()
        return {'message': 'Task created successfully'}, 201
    
    def delete(self, task_id):
        task = Tasks.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'message': 'Task deleted successfully'}
        return {'message': 'Task not found'}, 404
    
class AllTasksResource(Resource):
    def get(self):
        tasks = Tasks.query.all()
        tasks_list = []
        for task in tasks:
            tasks_list.append({'task_id': task.id, 'task_name': task.task_name, 'task_priority': task.task_priority})
        return tasks_list