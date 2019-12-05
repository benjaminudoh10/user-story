from user_story_app import app

@app.route('/')
def index():
    return 'It works!'
