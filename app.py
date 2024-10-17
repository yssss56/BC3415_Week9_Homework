from flask import Flask, render_template
import os

app = Flask(__name__)
contractaddress = os.getenv("CONTRACTADDRESS")
@app.route("/")
def index():
    return(render_template("index (Etherscan  - Sepolia Testnet - To Address).html", contractaddress=contractaddress))

if __name__ == "__main__":
    app.run()
