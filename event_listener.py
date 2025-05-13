from flask import Flask, request, jsonify
import os
from ada_neural_core import ADAEngine

app = Flask(__name__)
ada = ADAEngine()

# Root endpoint to confirm service is active
@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "QPRAS-ADA Webhook is live and accepting PayPal POST requests at /webhook/donation"
    })

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

        nudge_message = "Thank you for supporting ethical influence. Your contribution is shaping a new era of thought."
        ada.deploy_nudge("donation", nudge_message)

        return jsonify({"status": "success", "message": log_message}), 200

    except Exception as e:
        error_message = f"Error: {str(e)}"
        ada.log_external_event("PayPal", "WebhookError", error_message)
        return jsonify({"status": "error", "message": error_message}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
