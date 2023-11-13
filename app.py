from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/properties")
def properties():
    return render_template("properties-tab/property.html")


@app.route("/agents")
def agents():
    return render_template("agents-tab/agent.html")


@app.route("/calculator")
def calculator():
    return render_template("calcu-tab/calcu.html")


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)