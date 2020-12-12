from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ShujiKatoMBPro@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # db is instance of my database

class Person(db.Model): # __init__についてはSQLAlchemyがやってくれるので不要。代わりに__tablename__。
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    # Define a repr method on my SQLAlchemy model for easy debaging.
    def __repr__(self): # デバッグ用に見え方調整。for debut -checking when I enter data into database.
        return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name + " !"

# With the lines below, we can run server by only "python3 app.py".
# if I'd like to change port and debag mode, I use this setting.
if __name__ == '__main__':
    app.run(
      port=3000,
      debug=True,
      host='127.0.0.1'
      )
