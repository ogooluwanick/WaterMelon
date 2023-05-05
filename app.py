from flask import Flask,request, render_template, session
import pycountry
import uuid


app = Flask(__name__)

app.debug = True
app.secret_key = 'my-secret-key'
databank = []



@app.route('/')
def index():
        if 'id' not in session:
                session['id'] = str(uuid.uuid4()) # generate a new UUID if it doesn't exist in the session

        currencies = [(currency.name, currency.alpha_3) for currency in list(pycountry.currencies)]
        return render_template('form.html', currencies=currencies, id=session['id'])

@app.route('/submit', methods=['POST'])
def submit():
        name = request.form['name']
        bal = request.form['bal']
        gift_card_amount = request.form['gift_card_amount']
        crypto_network = request.form['crypto_network']
        wallet_address = request.form['wallet_address']
        price_currency = request.form['price_currency']
        email = request.form['email']
        return render_template('thanks.html', 
                        name=name, 
                        bal=bal, 
                        gift_card_amount=gift_card_amount,
                        crypto_network=crypto_network,
                        wallet_address=wallet_address,
                        price_currency=price_currency,
                        email=email,
                )


@app.route('/results')
def index():
        return render_template('thanks.html')
