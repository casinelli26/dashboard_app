from banking_app.src_v2 import db, models
from passlib.hash import pbkdf2_sha512
import re

class DatabaseQuery(object):
	@staticmethod
	def search_users(query):
		users = models.User.query.all()
		for user in users:
			if user.username == query:
				return user.username, user.password
		return 'None', 'None'

class Utils(object):

    @staticmethod
    def hash_password(password):
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha512.verify(password, hashed_password)