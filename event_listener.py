from flask import Flask, request, jsonify
from ada_neural_core import ADAEngine

app = Flask(__name__)
ada = ADAEngine()

@app.route("/webhook/donation", methods=["POST"])
def handle_donation():
    try:
        payload = request.json
        resource = payload.get("resource", {})

        amount = float(resource.get("amount", {}).get("value", 0.0))
        currency = resource.get("amount", {}).get("currency_code", "USD")
        payer = resource.get("payer", {}).get("email_address", "Anonymous")
        txn_id = resource.get("id", "N/A")

        log_message = f"{payer} donated {amount:.2f} {currency} (TXN: {txn_id})"
        ada.log_external_event("PayPal", "Donation", log_message)

        return jsonify({"status": "success", "message": log_message}), 200

    except Exception as e:
        ada.log_external_event("PayPal", "WebhookError", f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

# 🧠 Required block to run the Flask server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
