from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    raise Exception("500 Err0r")
    return jsonify(message="Hello level 400 FET, Quality Assurance!")


if __name__ == '__main__':
    app.run(debug=True)
