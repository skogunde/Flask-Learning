from flask import Flask, render_template, url_for, request
import csv
# render_template function allows us to send a html file. Create a folder templates and put the html file in it
# to print whatever is given in the parameter of the function, add a specific template line in index.html
# creating an instance of flask app
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world 2!!!'


@app.route('/index.html')
def my_home():
    return render_template('index.html')


@app.route('/about.html')
def about_me():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/components.html')
def components():
    return render_template('components.html')

@app.route('/projects.html')
def projects():
    return render_template('projects.html')

@app.route('/services.html')
def services():
    return render_template('services.html')

# Write the user entered information into our database.txt file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

# Write the user entered information into our database.csv file
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# To collect the information about contact details from user
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # collecting the user entered data
        data = request.form.to_dict()
        # Writing the user entered information into txt file
        write_to_file(data)
        # Writing the user entered information into csv file
        write_to_csv(data)
        # print(data)
        return 'Contact information submitted, Hoorayyyyyy!'
    else:
        return 'Something went wrong:-('