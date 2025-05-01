
# --- ADA Hyperdonor Integration ---

from ada_hyperdonor_interface import ADAHyperdonorInterface
from nudge_scheduler import NudgeScheduler
from influence_tracker import InfluenceTracker


class ADAEngine:
    def __init__(self):
        self.hyperdonor_module = ADAHyperdonorInterface()
        self.tracker = InfluenceTracker()
        self.scheduler = NudgeScheduler()
        self.donation_results = None

    def evaluate_funding_pathways(self):
        print("[ADA] Initiating Hyperdonor Simulation...")
        self.donation_results = self.hyperdonor_module.run_simulation()
        self.hyperdonor_module.summary()

        self.tracker.log_event(
            source="ADAEngine",
            event_type="Simulation Run",
            details=f"Simulation executed with {len(self.donation_results)} individuals"
        )

        # Generate and log a new nudge
        nudge = self.scheduler.generate_nudge()
        print(f"[ADA] Nudge Deployed ({nudge['type']}): {nudge['message']}")
        self.tracker.log_event(
            source="NudgeScheduler",
            event_type="Nudge Deployed",
            details=f"{nudge['type']}: {nudge['message']}"
        )

    def log_external_event(self, source, event_type, details):
        self.tracker.log_event(source, event_type, details)

        # Example learning logic: boost nudge type weight if linked to result
        if event_type == "Donation":
            self.scheduler.update_weights({"emotional": 0.1})
        elif event_type == "Contact":
            self.scheduler.update_weights({"visionary": 0.1})

    def get_potential_funding_summary(self):
        if self.donation_results is not None:
            return self.hyperdonor_module.get_high_probability_donors()
        else:
            return None
