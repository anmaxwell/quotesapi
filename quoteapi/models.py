from quoteapi import db

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return f"Quote('{self.id}', '{self.quote}')"