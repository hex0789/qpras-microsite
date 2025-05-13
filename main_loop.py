import time
from flask import Flask
import threading
from ada_neural_core import ADAEngine  # Make sure this import matches the correct path

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook listener is live!"

def run_flask():
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=5000)

def run_nudge_cycle():
    target_funding_goal = 100_000_000_000
    cumulative_donations = 0

    # Create an instance of ADAEngine (you can replace this with ADAHyperdonorInterface if needed)
    ada = ADAEngine()

    while cumulative_donations < target_funding_goal:
        # Simulate the campaign (this should now use the real webhook data)
        print("\n=== Iteration ===")
        print("Hyperdonor Campaign Simulation Results:")

        # Run the hyperdonor campaign with the ADA engine (no simulation)
        high_prob_df = ada.run_simulation()  # Ensure ADAEngine has the run_simulation method

        # Calculate total donations based on the probability
        donations_this_iter = high_prob_df['predicted_donation'].sum()
        cumulative_donations += donations_this_iter

        print(f"Total Donations (with >85% probability): ${cumulative_donations:,.2f}")
        print("[ADA] Nudge Deployed (visionary): Support a project shaping ethical influence — not by control, but by cognitive resonance.")
        
        # Sleep for 10 minutes (600 seconds)
        time.sleep(600)

if __name__ == "__main__":
    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True  # Allow the thread to exit when the main program exits
    flask_thread.start()

    # Start the nudge cycle
    run_nudge_cycle()
