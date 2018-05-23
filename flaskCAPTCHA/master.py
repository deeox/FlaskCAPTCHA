from flask import Flask, render_template, redirect, request, url_for, flash
import random as rnd

app = Flask(__name__)
n1 = rnd.randint(1, 99)
n2 = rnd.randint(1, 99)
n = n1 + n2


@app.route('/home/correct')
def correct():
    return render_template("correct.html")


@app.route('/home')
def home():
    return render_template("homepage.html", num1=n1, num2=n2)


@app.route('/home', methods=['POST'])
def homepage():
    value = request.form['input']
    print(n)
    print(value)
    if int(value) == int(n):
        return redirect('correct')
    else:
        return "Go back and try again"



