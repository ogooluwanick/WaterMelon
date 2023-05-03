from flask import Flask,request, render_template


app = Flask(__name__)

app.debug = True


@app.route('/')
def index():
        return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
        name = request.form['name']
        bal = request.form['bal']
        return render_template('thanks.html', name=name, bal=bal)
