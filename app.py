from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")


@app.route("/properties")
def properties():
    return render_template("properties-tab/property.html")




if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)