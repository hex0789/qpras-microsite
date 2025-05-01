
# main4.py – Adaptive Nudge Deployment & Learning Test

from engine.ada_neural_core import ADAEngine

def main():
    print("""\n=========================================
ADA Quantum Influence Engine [Adaptive Nudging]
=========================================""")

    # Initialize ADA Engine
    ada = ADAEngine()

    # Run Hyperdonor Simulation with Adaptive Nudge
    ada.evaluate_funding_pathways()

    # Log a Donation event to trigger learning
    ada.log_external_event(
        source="PayPal",
        event_type="Donation",
        details="Verified $500 donation via PayPal link"
    )

    # Log a Contact event to reinforce visionary strategy
    ada.log_external_event(
        source="Microsite",
        event_type="Contact",
        details="Outreach request from researcher via microsite form"
    )

    # Run again to see effect of learned weights
    ada.evaluate_funding_pathways()

    print("\n[ADA] Nudge history summary:")
    for nudge in ada.scheduler.get_recent_nudges():
        print(f"- {nudge['timestamp']} | {nudge['type']} | {nudge['message']}")

if __name__ == "__main__":
    main()
