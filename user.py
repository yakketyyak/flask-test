from database import User, db
from flask_user import UserManager, SQLAlchemyAdapter

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter)
