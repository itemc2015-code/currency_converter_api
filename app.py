from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():

    url = "https://v6.exchangerate-api.com/v6/ffdd5bbcb02e1b65d7f798ac/latest/USD"
    headers = {"api_key":"ffdd5bbcb02e1b65d7f798ac"}
    response = requests.get(url,headers=headers)
    rates = response.json()
    c_rates = rates['conversion_rates']

    currency_key = [c for c in c_rates.keys()]
    currency_value = [v for v in c_rates.values()]

    total_amount = None
    if request.method == 'POST':
        amount = request.form.get("amount")
        from_currency1 = request.form.get("from_currency")
        to_currency1 = request.form.get("to_currency")
        from_rates = c_rates[from_currency1]
        to_rates = c_rates[to_currency1]
        total_amount = float(amount) * (c_rates[to_currency1] / c_rates[from_currency1])
        total_amount = round(total_amount,2)

    return render_template('main.html',currency_key=currency_key,total_amount=total_amount,
                           from_currency1=from_currency1,to_currency1=to_currency1,
                           from_rates=from_rates,to_rates=to_rates)

if __name__ == '__main__':
    app.run(debug=True)