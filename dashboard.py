from database import db
from models import Recipe
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from datetime import datetime
from PIL import Image
import os


class Dashboard:
    @staticmethod
    @login_required

    def add_recipe():
        if request.method == 'POST':
            # save the uploaded image to a temporary location
            image_file = request.files['image']
            image_path = '/tmp/{}'.format(image_file.filename)
            image_file.save(image_path)

            # open the image using Pillow
            image = Image.open(image_path)

            # resize the image to a maximum width and height of 800 pixels
            width, height = image.size
            if width > 800 or height > 800:
                if width > height:
                    new_width = 800
                    new_height = int(height * (new_width / width))
                else:
                    new_height = 800
                    new_width = int(width * (new_height / height))
                image = image.resize((new_width, new_height))

            # convert the image to JPEG format
            image = image.convert('RGB')

            # save the resized and converted image to a new file
            image_filename = secure_filename(image_file.filename)
            print(1)
            print(image_filename)
            print(1)
            image_filename = os.path.splitext(image_filename)[0] + '.jpg'
            image_path = '/tmp/{}'.format(image_filename)
            image.save(image_path, format='JPEG')

            # create the recipe object
            recipe = Recipe(
                name=request.form['name'],
                image=open(image_path, 'rb').read(),
                description=request.form['description'],
                ingredients=request.form['ingredients'],
                instructions=request.form['instructions'],
                category=request.form['category'],
                tags=request.form['tags']
            )
            db.session.add(recipe)
            db.session.commit()

            # delete the temporary image file
            os.remove(image_path)

            flash('Recipe added successfully!', 'success')
            return redirect(url_for('dashboard'))

        return render_template('add_recipe.html')


