# RecipeApp-Kibo-TSP

The team project for Team Software project


**Install the dependencies using pip:**

pip install -r requirements.txt
## Signup, Login, and Logout Pages:

_The Recipe App allows users to create an account, login, and logout._

## 1. Signup Page:

The **Signup Page** is where users can create an account by providing: -_a unique username,_ -_a valid email address_, and -_a password._

Once the user has filled in the required fields and clicked on the **Signup button**, their information is saved in the database. If the user enters invalid information or leaves any field blank, an error message is displayed, prompting the user to correct the information.

## 2. Login Page:

The **Login Page** is where registered users can enter their username and password to access their account.

Once the user has filled in their details and clicked on the Login button, the application validates the information against the database.
**If the username and password match**, the user is redirected to the Recipe List Page and the dashboard. If the user enters invalid information or leaves any field blank, an error message is displayed, prompting the user to correct the information.

## 3. Logout Page:

The **Logout Page** is where users can log out of their account. Once the user has clicked on the Logout button, their session is destroyed, and they are redirected to the Login Page.

Additionally, a message is displayed to confirm that the user has successfully logged out.
