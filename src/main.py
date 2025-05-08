from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Webhook receiver is live."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # You can add logging, verification, and order execution logic here
    print(f"Received webhook: {data}")
    return jsonify({"status": "success", "data": data}), 200

if __name__ == '__main__':
    app.run()
