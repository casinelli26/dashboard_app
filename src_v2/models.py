from banking_app.src_v2 import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password = db.Column(db.String(120), index=True, unique=True)

	def __repr__(self):
		return '<User %r>' % (self.username)
