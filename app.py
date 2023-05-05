from flask import Flask,request, render_template, session
from builtins import enumerate  
import pycountry
import uuid



app = Flask(__name__)

app.secret_key = 'my-secret-key'
databank = []



@app.route('/')
def index():
        session['id'] = str(uuid.uuid4()) # generate a new UUID every time the function is called
        currencies = [(currency.name, currency.alpha_3) for currency in list(pycountry.currencies)]
        return render_template('form.html', currencies=currencies, id=session['id'])


@app.route('/submit', methods=['POST'])
def submit():
        name = request.form['name']
        bal = request.form['bal']
        gift_card_amount = request.form['gift_card_amount']
        price_currency = request.form['price_currency']
        crypto_network = request.form['crypto_network']
        wallet_address = request.form['wallet_address']
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

@app.route('/updateDB', methods=['POST'])
def update_db():
        data = request.get_json()
        survey_id = data['survey_id']
        
        # Check if the survey ID is already in the databank
        survey_index = next((i for i, entry in enumerate(databank) if entry['survey_id'] == survey_id), None)

        if survey_index is None:
                databank.append(data)
        else:
                databank[survey_index].update(data)

        return 'OK'


@app.route('/results')
def results():
    return render_template('results.html',databank=databank, enumerate=enumerate)


if __name__ == '__main__':
    app.run(debug=True)
