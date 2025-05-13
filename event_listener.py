import os
import json
from flask import Flask, request, jsonify
from paypalrestsdk import WebhookEvent

# Flask app setup
app = Flask(__name__)

# Your previous logic imports
from ada_neural_core import ADAEngine
from ada_hyperdonor_interface import ADAHyperdonorInterface

# Initialize the ADAEngine
ada = ADAEngine()

# Webhook route for PayPal notifications
@app.route('/webhook', methods=['POST'])
def paypal_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Paypal-Transmission-Sig')
    webhook_id = "6T150257H83796942"
    # Use the correct PayPal API to verify the event
    if WebhookEvent.verify(webhook_id, sig_header, payload):
        event = json.loads(payload)

        # Ensure the event type is what you are interested in
        if event['event_type'] == 'PAYMENT.SALE.COMPLETED':
            donation_data = event['resource']
            donor_name = donation_data['payer']['payer_info']['first_name']
            amount_donated = donation_data['amount']['total']
            
            print(f"Donation received from {donor_name} for ${amount_donated}")

            # Here you update the system with the real donation information
            ada.update_donations(donor_name, amount_donated)
            
            return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'failure'}), 400

# Method to update real donations
def update_donations(donor_name, amount_donated):
    # Update your model with the donation
    ada.add_donation(donor_name, amount_donated)

if __name__ == '__main__':
    app.run(debug=True)
