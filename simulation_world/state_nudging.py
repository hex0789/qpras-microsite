class RealitySimulator:
    def __init__(self):
        print("Reality Simulator Ready.\n")

    def nudge_probability(self, ada_response):
        score = ada_response["influence_score"]
        if score > 0.9:
            return "Local quantum field altered. Observable effect expected."
        elif score > 0.75:
            return "Probability fields nudged. Minor ripple in outcome likelihood."
        else:
            return "Insufficient coherence to alter reality."

