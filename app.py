from flask import Flask, jsonify, render_template
import random
from datetime import datetime

app = Flask(__name__)

stocks = ["Apple", "Google", "Microsoft", "Berkshire"]
previous_prices = {}

# API route: returns stock prices as JSON
@app.route("/stocks")
def get_stocks():
    stock_list = []
    for name in stocks:
        price = round(random.uniform(100, 1000), 2)
        arrow = ""
        if name in previous_prices:
            if price > previous_prices[name]:
                arrow = "↑"
            elif price < previous_prices[name]:
                arrow = "↓"
        previous_prices[name] = price
        stock_list.append({"Name": name, "Price": price, "Arrow": arrow})
    return jsonify(stock_list)

# Main page: renders HTML template
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
