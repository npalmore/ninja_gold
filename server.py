from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key="b'U\xcb\xbe\xadC6\r[7\xfc\xd6<q\xc0\xd7\x10"

@app.route('/')
def index():
    if 'userGold' not in session:
        session['userGold'] = 0
    if 'goldGen' not in session:
        session['goldGen'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    if 'farm' == request.form['building']:
        goldGen = random.randint(10,20)
        session['userGold'] += goldGen
        session['goldGen'] = goldGen
        print(goldGen)
        return redirect('/')
    elif 'cave' == request.form['building']:
        goldGen = random.randint(5,10)
        session['userGold'] += goldGen
        session['goldGen'] = goldGen
        print(goldGen)
        return redirect('/')
    elif 'house' == request.form['building']:
        goldGen = random.randint(2,5)
        session['userGold'] += goldGen
        session['goldGen'] = goldGen
        print(goldGen)
        return redirect('/')
    elif 'casino' == request.form['building']:
        goldGen = random.randint(-50,50)
        session['userGold'] += goldGen
        session['goldGen'] = goldGen
        print(goldGen)
        return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)