from flask import Flask, render_template, url_for, request, redirect
from Recommend import recommend

app = Flask(__name__)

variables = []


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/get-data', methods = ['GET','POST'])
def form_input():
    global variables
    variables.clear()
    bname = request.form['bname']
    bgenre = request.form['bgenre']
    variables.append(bname)
    variables.append(bgenre)
    return redirect('/books')

@app.route('/books',methods = ['GET','POST'])
def get_books():
    return render_template('books.html',books = recommend(variables))

if __name__ == "__main__":
    app.run()