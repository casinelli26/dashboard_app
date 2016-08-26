from flask import render_template, redirect, url_for, request, session
from banking_app.src_v2 import app
from banking_app.src_v2 import utils
from utils import DatabaseQuery, Utils
from banking_app.src_v2 import db, models
from .models import User
from banking_app.src_v2 import decorators
from decorators import login_required
from .form import LoginForm, RegistrationForm
import sys
sys.path.append('C://Users//J056883//Desktop//blackjack-0.0.1')

@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	if request.method == "POST":
		username = request.form['username']
		existing_user, _ = DatabaseQuery.search_users(username)
		if existing_user == 'None':
			password = request.form['password']
			password_confirm = request.form['password_confirm']
			if password != password_confirm:
				error = "Passwords do not match!"
				return render_template('register.html', title='register', error=error)
			password = Utils.hash_password(password)
			new_user = models.User(username=username, password=password)
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('login'))
		else:
			error = "Username has already been taken."
	return render_template('register.html', title='register', error=error)

@app.route('/logout')
def signout():
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == "POST":
		session['username'] = request.form['username']
		username = request.form['username']
		user_password = request.form['password']
		user, password = DatabaseQuery.search_users(username)
		try:
			if request.form['username'] != user or Utils.check_hashed_password(user_password, password) is False:
				error = "Invalid credentials"
		except ValueError:
			session['username'] = None
			error = "Your password did not encrpt properly."
			return render_template('login_page.html', error=error, title='login')
		else:
			return redirect(url_for('home'))
	return render_template('login_page.html', error=error, title='login')

@app.route('/test', methods=['GET', 'POST'])
def button_test():
	error = None
	return render_template('database_test.html')

@app.route('/home')
@login_required
def home():
	#print("PRINTING SESSION['USERNAME'] AT HOME PAGE " + session['username'])
	if 'username' not in session:
		print("SESSION DID NOT CARRY OVER DATA!")
	else:
		pass
		#print("THIS IS SESSION DATA AT HOME PAGE: {0}".format(session['username']))
	return render_template('dashboard.html')