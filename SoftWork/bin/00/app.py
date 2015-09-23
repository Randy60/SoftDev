from flask import Flask
import random
app = Flask(__name__)

@app.route("/home")
def home():
    page = ""
    page+="<h2> goddamn </h2>"   
    return page

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8009)
