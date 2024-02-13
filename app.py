from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define expected username and password
expected_username = "fair"
expected_password = "admin"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get username and password from the form
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if credentials are valid
        if username == expected_username and password == expected_password:
            # Redirect to welcome page
            return redirect(url_for('welcome', username=username))
        else:
            # Invalid credentials, render login page again
            return render_template('index.html')

    # Render login page for GET requests
    return render_template('index.html')

@app.route('/welcome/<username>')
def welcome(username):
    return f'<h1>Welcome, {username}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)


""" from flask import Flask, request, render_template

# app = Flask(__name__)
# from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If the form is submitted, retrieve the name from the form data
        name = request.form['name']
        return render_template('submitted.html', name=name)
    else:
        # If it's a GET request, render the form
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
 """