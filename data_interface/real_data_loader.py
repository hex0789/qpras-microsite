import pandas as pd
import numpy as np
import os

class RealWorldDataLoader:
    def __init__(self, scenario, data_folder="data"):
        self.data_folder = data_folder
        self.scenario = scenario
        self.csv_path = self.get_csv_for_scenario()
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"CSV not found at: {self.csv_path}")
        self.data = self.load_and_validate()

    def get_csv_for_scenario(self):
        scenario_file_map = {
            "Prevent Ecological Collapse": "prevent_ecological_collapse.csv",
            "Stabilize Global Markets": "stabilize_global_markets.csv",
            "Enhance Cognitive Evolution": "enhance_cognitive_evolution.csv",
            "Minimize Existential Risk": "minimize_existential_risk.csv"
        }
        scenario_file = scenario_file_map.get(self.scenario)
        if not scenario_file:
            raise ValueError(f"Unknown scenario: {self.scenario}")
        return os.path.join(self.data_folder, scenario_file)

    def load_and_validate(self):
        df = pd.read_csv(self.csv_path)
        required_cols = ['entanglement_density', 'phase_alignment', 'info_flow_1', 'info_flow_2']
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        df['entanglement_density'] = df['entanglement_density'].clip(0.0, 1.0)
        df['phase_alignment'] = df['phase_alignment'].clip(0.0, 1.0)
        df['info_flow_1'] = df['info_flow_1'].astype(int)
        df['info_flow_2'] = df['info_flow_2'].astype(int)
        return df

    def get_simulation_input(self, row_index=None):
        if self.data.empty:
            raise ValueError("Data is empty or failed to load.")

        row = self.data.sample(1).iloc[0] if row_index is None else self.data.iloc[row_index]
        return {
            'entanglement_density': float(row['entanglement_density']),
            'phase_alignment': float(row['phase_alignment']),
            'information_flow': [int(row['info_flow_1']), int(row['info_flow_2'])]
        }

    def get_all_data(self):
        return [
            {
                'entanglement_density': float(row['entanglement_density']),
                'phase_alignment': float(row['phase_alignment']),
                'information_flow': [int(row['info_flow_1']), int(row['info_flow_2'])]
            }
            for _, row in self.data.iterrows()
        ]
