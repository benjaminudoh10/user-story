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
    stories = db.relationship('Story', backref='user')

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


class Story(db.Model):
    '''
    This model describes a user story.
    '''
    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    type = db.Column(db.String, nullable=False)
    complexity = db.Column(db.String, nullable=False)
    eta = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    last_edited_by = db.Column(db.Column, db.ForeignKey('users.id'))
    assigned_for_approval = db.Column(db.Boolean, default=False)
    approved = db.Column(db.Boolean, nullable=True)

    @property
    def activated(self):
        return self.approved == True
    
    @property
    def inactive(self):
        return self.approved == False

    def to_json(self):
        result = {}
        result['id'] = self.id
        result['summary'] = self.summary
        result['description'] = self.description
        result['type'] = self.type
        result['complexity'] = self.complexity
        result['eta'] = self.eta.isoformat()
        result['cost'] = self.cost
        result['user'] = self.user.to_json()
        result['last_edited_by'] = self.user.to_json()
        result['assigned_for_approval'] = self.assigned_for_approval
        result['approved'] = self.approved
        return result
