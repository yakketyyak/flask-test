
from database import Role, db, User
from flask.blueprints import Blueprint
from datetime import datetime
from user import user_manager
from flask_user import roles_required, login_required



people = Blueprint('people', __name__,
                 template_folder='templates',
                 static_folder='static')


@people.route('/')
def test():
  role = Role.query.filter_by(name="ROLE_USER").first()
  if(role is None):
    role = Role()
    role.name = 'ROLE_USER'
    db.session.add(role)
    db.session.commit()  

  email = "email@gmail.com" + str(datetime.now().time())
  user_test = User()
  user_test.username = "Tom" + str(datetime.now().time())
  user_test.email = email
  user_test.password = user_manager.hash_password('Password1')
  user_test.confirmed_at = datetime.now()
  user_test.roles.append(role)
  db.session.add(user_test)
  db.session.commit()  
  user = User.query.filter_by(email=email).first()
  return "Test: Username %s " % user.username

@people.route('/test/role')
@roles_required('ROLE_USER') 
def test_role():
  role = Role.query.filter_by(name="ROLE_USER").first()
  return "Test: Username %s " % role.name

@people.route('/test/login')
@login_required
def test_login():
  role = Role.query.filter_by(name="ROLE_USER").first()
  return "Test: Username %s " % role.name
