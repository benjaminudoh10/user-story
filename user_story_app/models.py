from user_story_app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    '''
    This model describes a user.
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(
        db.String, nullable=False, unique=True, index=True)
    email = db.Column(
        db.String, nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String, nullable=False, default='user')

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}, {}>'.format(self.name, self.email)

    def to_json(self):
        result = {}
        result['id'] = self.id
        result['name'] = self.name
        result['phone'] = self.phone
        result['username'] = self.username
        result['email'] = self.email
        result['role'] = self.role
        return result
