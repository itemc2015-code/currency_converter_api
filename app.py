from flask import Flask,render_template,url_for,redirect
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():

    url = "https://v6.exchangerate-api.com/v6/ffdd5bbcb02e1b65d7f798ac/latest/USD"
    headers = {"api_key":"ffdd5bbcb02e1b65d7f798ac"}
    response = requests.get(url,headers=headers)
    rates = response.json()
    c_rates = rates['conversion_rates']

    currency_list = [c for c in c_rates.keys()]
    # print(c_rates)
    return render_template('main.html',currency_list=currency_list)

if __name__ == '__main__':
    app.run(debug=True)