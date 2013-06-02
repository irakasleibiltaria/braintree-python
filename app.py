import braintree

from flask import Flask, request, render_template
app = Flask(__name__)

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="d5d8qtntxknmcj4q",
                                  public_key="jx352kb8phnzw3mw",
                                  private_key="cda1a17a2bc39c0ab84ffe388e5ae6ab")

@app.route("/")
def form():
    return render_template("braintree.html")

@app.route("/create_transaction", methods=["POST"])
def create_transaction():
    result = braintree.Transaction.sale({
        "amount": "10.00",
        "credit_card": {
            "number": request.form["number"],
            "cvv": request.form["cvv"],
            "expiration_month": request.form["month"],
            "expiration_year": request.form["year"]
        },
        "options": {
            "submit_for_settlement": True
        }
    })
    if result.is_success:
        return "<h1>Success! Transaction ID: {0}</h1>".format(result.transaction.id)
    else:
        return "<h1>Error: {0}</h1>".format(result.message)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
