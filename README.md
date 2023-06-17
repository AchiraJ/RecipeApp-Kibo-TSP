
# RecipeApp-Kibo-TSP

This guide provides step-by-step instructions on how to run the RecipeApp application.  By following these instructions, you'll be able to set up and run your the app in no time.

## Prerequisites

Before running your Flask app, make sure you have the following prerequisites installed:

- Python: Flask requires Python 3.x. You can download the latest version of Python from the official website (https://www.python.org).

## Setup

Follow these steps to set up your Flask app:

1. **Create a virtual environment (optional but recommended):** It's good practice to create a virtual environment to isolate your Flask app's dependencies. Open your terminal or command prompt and run the following command to create a virtual environment named "venv":

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment (optional but recommended):** Activate the virtual environment to ensure that your Flask app uses the isolated environment.

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install Flask and required dependencies:** Run the following command to install Flask and its dependencies:

   ```bash
   pip install flask
   ```

## Run the Flask App

To run your Flask app, follow these steps:

1. **Set the Flask environment variable:** In your terminal or command prompt, run the following command:

   - On macOS and Linux:
     ```bash
     export FLASK_APP=app.py
     ```

   - On Windows:
     ```bash
     set FLASK_APP=app.py
     ```

2. **Enable debug mode (optional):** If you want to enable the debug mode, which provides detailed error messages, run the following command:

   - On macOS and Linux:
     ```bash
     export FLASK_ENV=development
     ```

   - On Windows:
     ```bash
     set FLASK_ENV=development
     ```

3. **Run the Flask app:** Start the Flask development server by executing the following command:

   ```bash
   flask run
   ```

4. **Access the Flask app:** Open your web browser and navigate to `http://localhost:5000` (or `http://127.0.0.1:5000`). You should see the "Hello, World!" message displayed in the browser.

Congratulations! You have successfully run your RecipeApp.


# App Navigation Guide

This guide will help you navigate through the RecipeApp. The app has a navigation bar at the top, which allows you to access different sections and features of the app.

## Home Page Navigation

When you open the app in your web browser, you'll see the home page with the following sections and features:

### Navigation Bar

The navigation bar provides links to various pages and features of the app. Here are the available options:

- **Home:** Clicking on "Home" will take you to the current page, the home page.

- **Featured recipes:** This link will take you to a page displaying featured recipes.

- **Recipe categories:** Clicking on this link will navigate you to a page showing different recipe categories.

- **Add recipe:** This link allows you to add a new recipe.

- **User profile:** Clicking on this link will take you to the user profile page.

- **Logout:** Hovering over this link will reveal a dropdown menu with the option to logout from the app.

- **About:** Clicking on this link will take you to the about page.

- **Contact:** Clicking on this link will navigate you to the contact page.

### Search Bar

The search bar allows you to search for specific recipes. Enter your search query in the search input field and click the "Search" button to initiate the search.

### Recipe Previews

The home page also displays a collection of recipe previews. Each preview consists of an image and the name of the recipe. Clicking on the recipe image or name will take you to the corresponding recipe page.

## Additional Notes

- The app uses Bootstrap for styling. You can find the Bootstrap CSS and JavaScript.


