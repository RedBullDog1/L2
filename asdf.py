from flask import Flask, request, jsonify
import dicttoxml
app = Flask(__name__)
@app.route("/currency", methods=["GET"])
def get_currency():
    content_type = request.headers.get("Content-Type")
    exchange_rate = {"currency": "USD", "rate": 43}
    if content_type == "application/json":
        return jsonify(exchange_rate)
    elif content_type == "application/xml":
        xml_data = dicttoxml.dicttoxml(exchange_rate, custom_root='exchange_rate', attr_type=False)
        return xml_data, 200, {'Content-Type': 'application/xml'}
    else:
        return "Курс валют: USD - 43"
if __name__ == '__main__':
    print("Сервер запущено на http://127.0.0.1:3222")
    app.run(port=3222)
