from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mySecret'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# define the user model


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    # Hash the password and store in the database
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # check if provided password is similar to stored password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)


# create the user table
with app.app_context():
    db.create_all()


# landing page
@app.route('/')
def index():
    return render_template('index.html')

# Signup page


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # check if the email is already in the database
        user = User.query.filter_by(email=email).first()
        if user:
            flash(
                'This email is already associated with an account. Please log in instead.')
            return redirect(url_for('login'))

        # # check if the username is already in the database
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists. Please try a different one.')
            return redirect(url_for('signup'))
        else:
            new_user = User(first_name=first_name, last_name=last_name,
                            username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Congratulations! Your account has been created.')
            return redirect(url_for('login'))
    return render_template('signup.html')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login page


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('You have been logged in successfully.')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')


# Logout page
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.')
    return redirect(url_for('index'))


# Dashboard page
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
