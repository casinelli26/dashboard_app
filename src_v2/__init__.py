from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.login import LoginManager, UserMixin, login_required

app = Flask(__name__)
app.secret_key = 'This is some kind of cool secret keyFDEfff'
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from banking_app.src_v2 import views, models