# hex_formula_sim.py

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
import numpy as np
import logging
from scipy.stats import entropy

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def build_entangled_circuit(num_qubits=2, depth=1):
    """
    Create a basic entangled quantum circuit with optional depth layers.
    """
    qc = QuantumCircuit(num_qubits)
    qc.h(0)
    qc.cx(0, 1)
    for _ in range(depth):
        qc.rx(np.random.uniform(0, np.pi), 0)
        qc.ry(np.random.uniform(0, np.pi), 1)
        qc.cz(0, 1)
    qc.measure_all()
    return qc

def generate_simulation_metrics():
    """
    Generate simulated metrics representing quantum reality parameters.
    """
    entanglement_density = np.round(np.random.uniform(0.4, 0.6), 4)
    phase_alignment = np.round(np.random.uniform(0.4, 0.6), 4)
    information_flow = [
        np.random.randint(480, 560),
        np.random.randint(440, 520)
    ]
    return entanglement_density, phase_alignment, information_flow

def compute_shannon_entropy(counts):
    """
    Compute Shannon entropy of measurement outcomes.
    """
    total = sum(counts.values())
    probs = np.array([v / total for v in counts.values()])
    return entropy(probs, base=2)

def scenario_weight_adjustments(scenario, entropy_value, info_flow):
    """
    Adjust entropy based on scenario-specific weights.
    """
    weight_map = {
        "Prevent Ecological Collapse": 1.15,
        "Stabilize Global Markets": 1.05,
        "Enhance Cognitive Evolution": 1.2,
        "Minimize Existential Risk": 1.1
    }
    weight = weight_map.get(scenario, 1.0)
    adjusted_entropy = round(entropy_value * weight, 4)
    variance = np.abs(info_flow[0] - info_flow[1])
    return adjusted_entropy, variance

def run_quantum_simulation(depth=1, scenario="Prevent Ecological Collapse"):
    """
    Run the quantum simulation and return metrics and results.
    """
    qc = build_entangled_circuit(depth=depth)
    simulator = Aer.get_backend('qasm_simulator')

    transpiled_qc = transpile(qc, simulator)
    qobj = assemble(transpiled_qc)

    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts()

    entanglement_density, phase_alignment, information_flow = generate_simulation_metrics()
    entropy_value = compute_shannon_entropy(counts)
    adjusted_entropy, variance = scenario_weight_adjustments(scenario, entropy_value, information_flow)

    quantum_output = {
        'entanglement_density': entanglement_density,
        'phase_alignment': phase_alignment,
        'information_flow': information_flow,
        'measurement_counts': counts,
        'entropy': round(entropy_value, 4),
        'adjusted_entropy': adjusted_entropy,
        'scenario_relevance': {
            'ecology_factor': np.round(entanglement_density * 1.2 - phase_alignment, 3),
            'market_variance': variance,
            'cognitive_signal_strength': np.round(phase_alignment * 0.9, 3)
        }
    }

    logging.info(f"Quantum Output: {quantum_output}")
    return quantum_output
