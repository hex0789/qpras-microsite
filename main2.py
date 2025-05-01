
# main2.py – ADA Hyperdonor Simulation Entry Point

from engine.ada_neural_core import ADAEngine

def main():
    print("""\n==============================
ADA Quantum Influence System
==============================\n""")
    
    # Initialize the ADA Engine
    ada = ADAEngine()
    
    # Run Hyperdonor Simulation
    ada.evaluate_funding_pathways()
    
    # Retrieve and display summary
    summary = ada.get_potential_funding_summary()
    if summary is not None and not summary.empty:
        print("\n=== High-Probability Donor Summary Table ===")
        print(summary.to_string(index=False))
    else:
        print("\n[ADA] No high-probability donations identified above threshold.")

if __name__ == "__main__":
    main()
