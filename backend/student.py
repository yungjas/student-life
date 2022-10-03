from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    # should be binding to 0.0.0.0 if you want the container to be accessible from outside
    app.run(host="0.0.0.0", port=6000, debug=True)
