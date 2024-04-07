from flask import Flask
from extensions import db, Api
from tasks import TaskResource, AllTasksResource
from owner import OwnerResource, AllOwners
from config import Config

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # SQLite database file
app.config.from_object(Config)
db.init_app(app)    
api = Api(app)

api.add_resource(TaskResource, '/tasks/<int:task_id>')
api.add_resource(AllTasksResource, '/tasks/')
api.add_resource(OwnerResource, '/owner/<int:owner_id>')
api.add_resource(AllOwners, '/owners/')

if __name__ == '__main__':
    app.run(debug=True)

