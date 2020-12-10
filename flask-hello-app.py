from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


# With the lines below, we can run server by only "python3 app.py".
if __name__ == '__main__':
    app.run(
      port=3000,
      debug=True,
      host='127.0.0.1'
      )
