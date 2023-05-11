from flask import render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import *
from dashboard import *
from database import db, app
from flask_mail import Message, Mail
from recipes import *

# app configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mySecret'
# mail configuration for resettng password
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'achirajonathan@gmail.com'
app.config['MAIL_PASSWORD'] = 'gvmvafpcrmzkhblr'
mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# create the user table and user reset tables

with app.app_context():
    db.init_app(app)
    db.create_all()
    # clear_database()
    populate_data(db)


def send_password_reset_email(user, token):
    msg = Message('Password Reset Request',
                  sender='achirajonathan@gmail.com', recipients=[user.email])
    msg.body = f'''Dear {user.first_name},

        We have received a request to reset the password for your account (Username: {user.username}). 
        To proceed with resetting your password, please click the link below:

        {url_for('reset_password', token=token, _external=True)}
        
        The reset link expires in 3 minutes.

        If you did not make this request, please ignore this email.

        Thank you,
        The RecipeApp Team
        '''
    mail.send(msg)


# landing page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('dashboard.html')


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
            flash('Invalid username or password. Please try again.', 'danger')
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

# forgot password page


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            token = user.get_reset_password_token()
            send_password_reset_email(user, token)
            flash('An email has been sent with instructions to reset your password.')
            return redirect(url_for('login'))
        else:
            flash('No user found with that email address.')
            return redirect(url_for('forgot_password'))
    return render_template('forgot_password.html')
# reset password page


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    user = User.verify_reset_password_token(token)
    if not user:
        flash('Invalid or expired token.')
        return redirect(url_for('forgot_password'))
    if request.method == 'POST':
        password = request.form['password']
        user.set_password(password)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', token=token)


@app.route('/add_recipe2', methods=['GET', 'POST'])
@login_required
def add_recipe2():
    return Dashboard.add_recipe2()

@app.route('/dashboard', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_string = request.form['search']
        recipes = Recipes.query.filter(Recipes.title.ilike(f'%{search_string}%')).all()
        return render_template('dashboard.html', recipes=recipes, search_string=search_string, user=current_user)
    else:
        return render_template('dashboard.html', user=current_user)


if __name__ == '__main__':
        
    app.run(debug=True)
