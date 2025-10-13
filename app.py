from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to your Flask API!"

@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
