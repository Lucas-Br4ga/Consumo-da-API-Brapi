from flask import Flask, request, render_template, redirect, url_for
from api.fetch_data import get_bravi_data

app = Flask(__name__)

@app.route("/")
def homepage():
    tickers = ["AZUL4", "CRFB3", "HAPV3", "COGN3", "B3SA3", "ITSA4", "PETR4"]
    token = "tDnPn8svhk5z7kS7izU1yC"

    data = get_bravi_data(tickers=tickers,token=token)
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)