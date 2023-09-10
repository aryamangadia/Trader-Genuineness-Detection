# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
from fileinput import filename
import os

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Hello World'

@app.route('/sec')
# ‘/’ URL is bound with hello_world() function.
def hello_everyone():
	return 'Hello Everyone'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route("/home")
def index():
    return render_template("index.html")

@app.route('/homepage', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       name = request.form.get("name")
       # getting input with name = lname in HTML form
       address = request.form.get("address")
       os.mkdir("proof_documents/"+name)
       gst_file = request.files['gst_file']
       gst_file.save("proof_documents/"+name+"/user_gst_proof.pdf")  

       return "Your name is "+name +" "+ address
    return render_template("index.html")
 
# @app.route('/success', methods = ['POST'])  
# def success():  
#     if request.method == 'POST':  
#         f = request.files['file']
#         f.save(f.filename)  
#         return render_template("Acknowledgement.html", name = f.filename)  
  

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
      










      

# from distutils.log import debug
# from fileinput import filename
# from flask import *
# app = Flask(__name__)

# @app.route('/')
# def main():
# 	return render_template("tester.html")

# @app.route('/success', methods = ['POST'])
# def success():
# 	if request.method == 'POST':
# 		f = request.files['file']
# 		f.save(f.filename)
# 		return render_template("Acknowledgement.html", name = f.filename)

# if __name__ == '__main__':
# 	app.run(debug=True)

