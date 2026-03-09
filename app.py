from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Python Add Two Numbers API"

@app.route('/add', methods=['GET'])
def add():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run()