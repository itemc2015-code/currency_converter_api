from flask import Flask,render_template,request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/',methods=['GET','POST'])
def home():
    try:
        url = os.getenv("api_url")
        headers = os.getenv("api_header")
        response = requests.get(url,headers=headers)
        rates = response.json()
        c_rates = rates['conversion_rates']
    except Exception as e:
        return f"API error {e}"

    currency_key = [c for c in c_rates.keys()]
    currency_value = [v for v in c_rates.values()]

    total_amount = None
    from_rates = None
    to_rates = None

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
    app.run(debug=False,host="0.0.0.0",port=5000)