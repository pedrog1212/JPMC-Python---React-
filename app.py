from flask import Flask, request, render_template

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
