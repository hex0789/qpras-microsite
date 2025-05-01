
# main3.py – ADAEngine Test with InfluenceTracker

from engine.ada_neural_core import ADAEngine

def main():
    print("""\n==============================
ADA Quantum Influence System [Tracker Enabled]
==============================\n""")

    # Initialize ADA Engine
    ada = ADAEngine()

    # Run the simulation (automatically logs internally)
    ada.evaluate_funding_pathways()

    # Simulate an external trigger (e.g., real-world donation)
    ada.log_external_event(
        source="PayPal",
        event_type="Donation",
        details="Received anonymous donation of $1,000"
    )

    # Simulate a contact form submission
    ada.log_external_event(
        source="Microsite",
        event_type="Contact",
        details="New outreach message from an HNWI rep"
    )

    print("\n[ADA] Convergence events logged successfully.")

if __name__ == "__main__":
    main()
