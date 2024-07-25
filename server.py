from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/about")
def blog():
    return render_template('about.html')

@app.route("/submit_form", methods =['POST','GET'])
def submit_form():
   
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        
        return "<p id='successmsg'>Form submitted successfully!</p>"
    else:
        return "<p id='successmsg'>Ooops, Something went wrong!</p>"