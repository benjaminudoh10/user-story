import flask_restplus

from user_story_app import app, db, api

story_api = api.namespace('story', description='Story API')

user = api.model('User', {
    'id': flask_restplus.fields.String(
        required=True, description='The id of the user',
        attribute='user_id'),
    'name': flask_restplus.fields.String(
        description='The full name of the story', attribute='name'),
    'username': flask_restplus.fields.String(
        description='Unique username for the user',
        attribute='username'),
    'email': flask_restplus.fields.String(
        description='Email address for the user',
        attribute='email'),
    'role': flask_restplus.fields.String(
        description='The role of the user',
        enum=['user', 'admin'], attribute='role')
})

story_schema = api.model('Story', {
    'id': flask_restplus.fields.String(
        required=True, description='The id of the story',
        attribute='story_id'),
    'summary': flask_restplus.fields.String(
        description='A summary of the story', attribute='summary'),
    'description': flask_restplus.fields.String(
        description='Detailed description of the story',
        attribute='description'),
    'type': flask_restplus.fields.String(
        description='The type the story belongs to',
        enum=['enhancement', 'bugfix', 'development', 'qa'],
        attribute='type'),
    'complexity': flask_restplus.fields.String(
        description='The complexity of the story',
        enum=['difficult', 'easy', 'np-hard'],
        attribute='complexity'),
    'eta': flask_restplus.fields.Date(
        dt_format='iso8601',
        description='Expected time of completion for the story',
        attribute='eta'),
    'cost': flask_restplus.fields.Integer(
        description='Cost of getting the story done',
        attribute='cost'),
    'user': flask_restplus.fields.Nested(
        user,
        description='The creator of the story',
        attribute='user'),
    'last_edited_by': flask_restplus.fields.Nested(
        user,
        description='The user who last edited this story',
        attribute='last_edited_by'),
    'assigned_for_approval': flask_restplus.fields.String(
        description='Indicates if the story has been assigned for approval',
        attribute='assigned_for_approval'),
    'approved': flask_restplus.fields.String(
        description='Indicates if the story has been approved by admin',
        attribute='complexity', default=False)
})


@app.route('/')
def index():
    return 'It works!'


@story_api.route('/<story_id>')
class Story(flask_restplus.Resource):

    @story_api.marshal_with(story_schema)
    def get(self, story_id):
        """
        Endpoint to get information about a story
        """
        return {'story_id': '45'}
