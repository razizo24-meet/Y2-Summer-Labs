from flask import Flask, render_template,request,redirect,url_for
from flask import session as login_session

import random 

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'yo'

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    else:
        username = request.form['username']
        password = request.form['passwrod']
        if username ==  'razi' :
            login_session['admin'] = True
            return redirect(url_for('home'))
        else:
            login_session['admin'] = False
            return redirect(url_for('home'))


@app.route("/home",methods =['GET','POST'])
def home():
    return render_template("home.html", admin = login_session['admin'])

@app.route("/faith/<birth>")
def faith(birth):
    fortunes = [
    "Today is your lucky day!",
    "A thrilling time is in your near future.",
    "Happiness is just around the corner.",
    "Success is on your path.",
    "You will meet someone special soon.",
    "An exciting opportunity awaits you.",
    "Good news will come your way soon.",
    "You will achieve your goals.",
    "A pleasant surprise is in store for you.",
    "New friendships are on the horizon."  ]
    
    wanted_for =  "New friendships are on the horizon."
    birth_len = len(birth)
    if birth_len < 10:
        wanted_for =fortunes[birth_len-1]

    
    return render_template("faith.html",wanted_for = wanted_for )


if __name__ == "__main__":
    app.run(debug=True)
    
   