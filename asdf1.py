from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

def fetch_exchange_rate(date):
    api_url = (
        f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json&date={date.strftime('%Y%m%d')}&valcode=USD"
    )
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0].get("rate")
    return None

# Route to handle currency exchange rate requests
@app.route("/currency", methods=["GET"])
def get_currency_rate():
    param = request.args.get("param")
    today = datetime.today()

    if param == "today":
        exchange_rate = fetch_exchange_rate(today)
        if exchange_rate is not None:
            return jsonify({
                "date": today.strftime('%Y-%m-%d'),
                "currency": "USD",
                "rate": exchange_rate
            })
        else:
            return jsonify({"error": "Unable to retrieve the exchange rate for today."}), 500

    elif param == "yesterday":
        yesterday = today - timedelta(days=1)
        exchange_rate = fetch_exchange_rate(yesterday)
        if exchange_rate is not None:
            return jsonify({
                "date": yesterday.strftime('%Y-%m-%d'),
                "currency": "USD",
                "rate": exchange_rate
            })
        else:
            return jsonify({"error": "Unable to retrieve the exchange rate for yesterday."}), 500

    else:
        return jsonify({"error": "Invalid parameter. Use 'today' or 'yesterday'."}), 400

if __name__ == "__main__":
    app.run(port=3222)
