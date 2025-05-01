
import pandas as pd
from qpras_hyperdonor_module import simulate_hyperdonor_campaign

class ADAHyperdonorInterface:
    def __init__(self, threshold=0.85):
        self.threshold = threshold
        self.simulation_results = None
        self.total_donations = 0.0

    def run_simulation(self):
        df, total = simulate_hyperdonor_campaign()
        self.simulation_results = df
        self.total_donations = total
        return df

    def get_high_probability_donors(self):
        if self.simulation_results is not None:
            return self.simulation_results[self.simulation_results["probability_of_success"] > self.threshold]
        else:
            return pd.DataFrame()

    def summary(self):
        donors = self.get_high_probability_donors()
        print("=== ADA Hyperdonor Summary ===")
        print(donors[["name", "predicted_donation", "probability_of_success"]])
        print(f"Total High-Probability Donations: ${self.total_donations:,.2f}")
