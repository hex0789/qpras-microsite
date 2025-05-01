
from flask import Flask, request, jsonify
from ada_neural_core import ADAEngine

app = Flask(__name__)
ada = ADAEngine()

@app.route('/webhook/donation', methods=['POST'])
def handle_donation():
    data = request.json
    amount = data.get('amount')
    donor = data.get('donor', 'Anonymous')
    detail = f"Live donation of ${amount} from {donor}"
    ada.log_external_event("PayPal", "Donation", detail)
    return jsonify({"status": "logged", "detail": detail}), 200

@app.route('/webhook/contact', methods=['POST'])
def handle_contact():
    data = request.json
    name = data.get('name', 'Unknown')
    message = data.get('message')
    detail = f"Message from {name}: {message}"
    ada.log_external_event("Microsite", "Contact", detail)
    return jsonify({"status": "logged", "detail": detail}), 200

@app.route('/')
def index():
    return "QPRAS-ADA Webhook Listener Active", 200

if __name__ == "__main__":
    app.run(port=5001)
