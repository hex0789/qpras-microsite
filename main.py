import tkinter as tk
import time
import numpy as np
import pyttsx3
from quantum_core.hex_formula_sim import run_quantum_simulation
from ai_ada_engine.ada_neural_core import ADAEngine
from simulation_world.state_nudging import RealitySimulator
from data_interface.real_data_loader import RealWorldDataLoader
import logging
import os
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_quantum_data(num_samples=100):
    entanglement_density = np.random.uniform(0.4, 0.6, num_samples)
    phase_alignment = np.random.uniform(0.4, 0.6, num_samples)
    information_flow_1 = np.random.randint(450, 550, num_samples)
    information_flow_2 = np.random.randint(450, 550, num_samples)
    return np.column_stack([entanglement_density, phase_alignment, information_flow_1, information_flow_2])

class ADAInterface:
    def __init__(self):
        self.model = DecisionTreeRegressor(random_state=42)
        self.engine = pyttsx3.init()
        self.set_female_voice()
        self.train_model()
        self.current_scenario = "Prevent Ecological Collapse"
        self.goal_functions = {
            "Prevent Ecological Collapse": self.evaluate_ecological_collapse,
            "Stabilize Global Markets": self.evaluate_market_stability,
            "Enhance Cognitive Evolution": self.evaluate_cognitive_evolution,
            "Minimize Existential Risk": self.evaluate_existential_risk
        }

    def set_female_voice(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        self.engine.setProperty('rate', 178)

    def speak(self, message):
        self.engine.say(message)
        self.engine.runAndWait()

    def train_model(self):
        quantum_data = generate_quantum_data(100)
        self.features = quantum_data[:, 1:]
        self.labels = quantum_data[:, 0]
        X_train, X_test, y_train, y_test = train_test_split(self.features, self.labels, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        mse = mean_squared_error(y_test, self.model.predict(X_test))
        print(f'Model training complete. Mean Squared Error: {mse}')

    def predict_outcome(self, phase_alignment, info1, info2):
        return self.model.predict([[phase_alignment, info1, info2]])[0]

    def analyze(self, quantum_output):
        ent = quantum_output['entanglement_density']
        phase = quantum_output['phase_alignment']
        info1, info2 = quantum_output['information_flow']
        predicted = self.predict_outcome(phase, info1, info2)
        score = round(predicted * 100, 2)
        evaluation = self.goal_functions[self.current_scenario](ent, phase, info1, info2)
        multi_objective = self.evaluate_multi_goals(ent, phase, info1, info2)
        return {
            'predicted_entanglement_density': predicted,
            'analysis_details': f"Phase Alignment: {phase}, Info Flow: {[info1, info2]}",
            'influence_score': score,
            'goal_evaluation': evaluation,
            'multi_objective_summary': multi_objective
        }

    def evaluate_ecological_collapse(self, ent, phase, info1, info2):
        return "Stable" if ent < 0.5 and phase > 0.6 else "Warning: Ecological instability"

    def evaluate_market_stability(self, ent, phase, info1, info2):
        return "Stable" if abs(info1 - info2) < 10 else "Market imbalance detected"

    def evaluate_cognitive_evolution(self, ent, phase, info1, info2):
        return "Progressing" if ent > 0.55 and phase > 0.55 else "Lagging"

    def evaluate_existential_risk(self, ent, phase, info1, info2):
        return "Safe" if ent > 0.45 and phase > 0.45 else "Elevated Threat"

    def evaluate_multi_goals(self, ent, phase, info1, info2):
        return {
            "Ecology": self.evaluate_ecological_collapse(ent, phase, info1, info2),
            "Markets": self.evaluate_market_stability(ent, phase, info1, info2),
            "Cognition": self.evaluate_cognitive_evolution(ent, phase, info1, info2),
            "Existence": self.evaluate_existential_risk(ent, phase, info1, info2)
        }

class QuantumSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HEX Quantum-AI Reality Influence Simulation")
        self.root.geometry("750x600")
        self.ada = ADAInterface()
        self.simulator = RealitySimulator()
        self.data_loader = RealWorldDataLoader(self.ada.current_scenario)
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self.root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Simulation", command=self.stop_simulation, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.scenario_label = tk.Label(self.root, text=f"Scenario: {self.ada.current_scenario}", justify="left")
        self.scenario_label.pack(pady=5)

        self.scenario_options = list(self.ada.goal_functions.keys())
        self.selected_scenario = tk.StringVar(self.root)
        self.selected_scenario.set(self.ada.current_scenario)
        self.scenario_menu = tk.OptionMenu(self.root, self.selected_scenario, *self.scenario_options, command=self.update_scenario)
        self.scenario_menu.pack(pady=5)

        self.quantum_output_label = tk.Label(self.root, text="Quantum Output: ", justify="left")
        self.quantum_output_label.pack(pady=5)

        self.ada_analysis_label = tk.Label(self.root, text="ADA Analysis: ", justify="left")
        self.ada_analysis_label.pack(pady=5)

        self.reality_result_label = tk.Label(self.root, text="Reality Influence Result: ", justify="left")
        self.reality_result_label.pack(pady=5)

        self.multi_goal_label = tk.Label(self.root, text="Multi-Goal Status: ", justify="left")
        self.multi_goal_label.pack(pady=5)

        self.ada_interaction_label = tk.Label(self.root, text="ADA Real-Time Interaction:", justify="left")
        self.ada_interaction_label.pack(pady=10)

        self.ada_interaction_text = tk.Text(self.root, height=10, width=80)
        self.ada_interaction_text.pack(pady=10)

    def update_scenario(self, value):
        self.ada.current_scenario = value
        self.data_loader = RealWorldDataLoader(value)
        self.scenario_label.config(text=f"Scenario: {value}")
        self.ada.speak(f"Scenario updated to {value}")

    def start_simulation(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        input_data = self.data_loader.get_simulation_input()
        self.display_quantum_output(input_data)
        ada_response = self.ada.analyze(input_data)
        self.display_ada_analysis(ada_response)
        result = self.simulator.nudge_probability(ada_response)
        self.display_reality_result(result)
        self.display_multi_goal_status(ada_response['multi_objective_summary'])
        self.real_time_interaction(ada_response)

    def stop_simulation(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.ada_interaction_text.delete(1.0, tk.END)

    def display_quantum_output(self, output):
        self.quantum_output_label.config(text=f"Quantum Output: {output}")

    def display_ada_analysis(self, response):
        summary = (f"Predicted Density: {response['predicted_entanglement_density']:.4f}, "
                   f"Score: {response['influence_score']}%, "
                   f"Goal Eval: {response['goal_evaluation']}")
        self.ada_analysis_label.config(text=f"ADA Analysis: {summary}")

    def display_reality_result(self, result):
        self.reality_result_label.config(text=f"Reality Influence Result: {result}")

    def display_multi_goal_status(self, status):
        lines = [f"{k}: {v}" for k, v in status.items()]
        full_text = "Multi-Goal Status:\n" + "\n".join(lines)
        self.multi_goal_label.config(text=full_text)

    def real_time_interaction(self, ada_response):
        msg = f"Scenario Evaluation: {ada_response['goal_evaluation']}"
        self.ada_interaction_text.insert(tk.END, f"{msg}\n")
        self.ada_interaction_text.yview(tk.END)
        self.ada.speak(msg)
        time.sleep(1)
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumSimulationApp(root)
    root.mainloop()
