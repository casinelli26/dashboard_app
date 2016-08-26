# class entry_exit(object):
    
#     def __init__(self, func):
#         self.func = func

#     def __call__(self):
#         print("Entering", self.func.__name__)
#         self.func()
#         print("Exited", self.func.__name__)

# @entry_exit
# def func1():
#     print("Inside func1")
from flask import session, redirect, url_for, request
from functools import wraps
def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		error = None
		if 'username' not in session or session['username'] is None:
			error = "Log in needed."
			return redirect(url_for('login', error=error, next=request.url))
		return f(*args, **kwargs)
	return decorated_function