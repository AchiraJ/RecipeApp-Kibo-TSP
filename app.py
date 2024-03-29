from flask import render_template, request, redirect, url_for, flash , Flask
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import *
from dashboard import *
from database import db, app
from flask_mail import Message, Mail
from recipes import *
import random, os
from werkzeug.utils import secure_filename
from sqlalchemy import func

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

# Image upload configuration
app.config['UPLOAD_FOLDER'] = 'static/recipe_images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

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



# Home page
@app.route('/', methods=['GET'])
def home():
    category = 'Breakfast'  # Choose the desired category
    recipes_per_category = 6  # Choose the number of recipes to display per category

    recipes = Recipes.query.filter_by(category=category).limit(recipes_per_category).all()

    return render_template('home.html', recipes=recipes)

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
            with app.test_request_context():
                flash('You have been logged in successfully.', 'clear')
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
    return redirect(url_for('home'))


# Dashboard page
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    categories = ['Breakfast', 'Lunch', 'Dinner', 'Dessert']
    results = []
    selected_recipes = set()  # To store the selected recipe IDs
    recipes_per_category = 3

    for category in categories:
        recipes = Recipes.query.filter_by(category=category).all()

        # Exclude previously selected recipes from the same category
        available_recipes = [recipe for recipe in recipes if recipe.id not in selected_recipes and recipe.category == category]

        if len(available_recipes) > 0:
            # Select up to 3 random recipes from the available recipes
            random_recipes = random.sample(available_recipes, min(recipes_per_category, len(available_recipes)))
            selected_recipes.update(recipe.id for recipe in random_recipes)
            results.extend(random_recipes)

        if len(results) == 9:
            break

    return render_template('dashboard.html', user=current_user, results=results)


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

# search
@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('query', '')

    if query.strip() == '':
        results = []
    else:
        results = Recipes.query.filter(
            (Recipes.name.ilike(f'%{query}%')) |
            (Recipes.category.ilike(f'%{query}%')) |
            (Recipes.image_name.ilike(f'%{query}%')) |
            (Recipes.ingredients.ilike(f'%{query}%')) |
            (Recipes.instructions.ilike(f'%{query}%'))
        ).all()

    return render_template('search_results.html', results=results, query=query)

def valid_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


# Add recipe
@app.route('/add_recipe2', methods=['GET','POST'])
@login_required
def add_recipe2():
    if request.method == 'POST':
        name = request.form.get('name')
        image_name = request.form.get('image_name')
        category = request.form.get('category')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        
        # Check if recipe already exists in the database
        recipe = Recipes.query.filter_by(name=name).first()
        if recipe:
            # Delete existing recipe and related data from the database
            db.session.delete(recipe)
        
        # Delete all related data that matches the existing recipe name
        Recipes.query.filter_by(name=name).delete()

        # Save the uploaded image
        image = request.files.get('image_name')
        
        if image and valid_file(image.filename):
            image_name = image.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
            image.save(image_path)
        else:
            image_name = None
            image_path = None
            flash('Invalid file. Only PNG, JPG, JPEG, and GIF images are allowed.')
        
        
        # Add new recipe to the database
        new_recipe = Recipes(name=name, image_name = image_name , category=category, ingredients=ingredients, instructions=instructions)
        db.session.add(new_recipe)
        db.session.commit()
        
        return redirect(url_for('dashboard'))
    return render_template('add_recipe2.html')

# List recipe with details on click
@app.route('/recipe', methods=['GET', 'POST'])
@login_required
def recipe():
    recipe_id = int(request.args.get('id'))
    recipe = Recipes.query.get(recipe_id)
    return render_template('recipe.html', recipe=recipe)

#Search by category
@app.route('/category', methods=['GET', 'POST'])
def search_category():
    if request.method == 'POST':
        category = request.form['meal_type']
        recipes = Recipes.query.filter_by(category=category).all()
        return render_template('search_category.html', recipes=recipes, category=category, user=current_user)
    else:
        return render_template('search_category.html', user=current_user)


# Featured recipes

@app.route('/featured-recipes', methods=['GET', 'POST'])
def featured_recipe():
    recipes = Recipes.query.order_by(func.random()).limit(6).all()
    return render_template('featured_recipes.html', recipes=recipes)

# View recipe route
@app.route('/view_recipe/<recipe_id>')
@login_required
def view_recipe(recipe_id):
    recipe = Recipes.query.get(recipe_id)
    if recipe:
        return render_template('view_recipe.html', recipe=recipe)
    else:
        flash('Recipe not found.', 'danger')
        return redirect(url_for('dashboard'))



if __name__ == '__main__':
        
    app.run(debug=True)

