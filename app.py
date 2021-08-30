from database import db
from flask import Flask
from views import people
from user import user_manager

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://metis:metis@postgres:5432/metis_db"
    app.config['SECRET_KEY']="Test"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    register_extensions(app)
    register_blueprints(app)
    return app 

def register_extensions(app):
    db.init_app(app)    

def register_blueprints(app):
    app.register_blueprint(people, url_prefix='')

def setup_database(app):
    with app.app_context():
        db.create_all()
        print('DB create all tables in database {}'.format(db))

if __name__ == '__main__':
    app = create_app()
    user_manager.init_app(app)
    setup_database(app)
    app.run(host='0.0.0.0')
