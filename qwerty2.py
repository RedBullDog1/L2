from flask import Flask, request

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def get_currency():
    today = request.args.get("today")
    key = request.args.get("key")
    exchange_rate = "USD - 43"
    response = (
        f"<h1>Курс валют</h1>"
        f"<p><b>Курс:</b> {exchange_rate}</p>"
        f"<p><b>Параметри:</b> today={today}, key={key}</p>"
    )
    return response
if __name__ == '__main__':
    print("Сервер запущено на http://127.0.0.1:3222")
    app.run(port=3222)