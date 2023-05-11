from database import db
from models import Recipes
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from datetime import datetime

import os


class Dashboard:
    @staticmethod
    @login_required

    def add_recipe2():
        if request.method == 'POST':
                # create the recipe object
                recipe = Recipes(
                    name=request.form['name'],
                    ingredients=request.form['ingredients'],
                    instructions=request.form['instructions'],
                    category=request.form['category'],
                )
                db.session.add(recipe)
                db.session.commit()

                flash('Recipe added successfully!', 'success')
                return redirect(url_for('dashboard'))
        
        return render_template('add_recipe2.html')


