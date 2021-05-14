from quoteapi import app, db
from quoteapi.models import Quote
from flask import jsonify, request, redirect, url_for
from random import randrange

#test quotes
#quotes = ["The Best Way To Get Started Is To Quit Talking And Begin Doing.", "Dont Let Yesterday Take Up Too Much Of Today.", "Its Not Whether You Get Knocked Down, Its Whether You Get Up.", "Knowing Is Not Enough; We Must Apply. Wishing Is Not Enough; We Must Do."]

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/api/quote")
def quote():
    quotec_count = Quote.query.count()
    quote_no = randrange(quotec_count)-1
    text = Quote.query.filter_by(id=int(quote_no)).first()

    #return str(text.quote)
    return jsonify(index=quote_no,quote=str(text.quote))

@app.route("/api/addquote", methods=['GET', 'POST'])
def add_quote():

    #newquote = request.json
    #newquote['quote']

    newquote = Quote(quote=request.json['quote'])
    db.session.add(newquote)
    db.session.commit()

    return redirect(url_for('home'))