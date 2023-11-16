from models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user
    return None

def create_user(username, email, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, email=email, password=hashed_password)
    return user