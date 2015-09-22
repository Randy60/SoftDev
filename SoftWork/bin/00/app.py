from flask import Flask
app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1>Sup Bro</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8602)
