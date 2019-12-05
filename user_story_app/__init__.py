from flask import Flask

app = Flask(__name__)

from user_story_app import routes
