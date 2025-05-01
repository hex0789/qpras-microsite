
import random
import datetime

class NudgeScheduler:
    def __init__(self):
        self.nudge_history = []
        self.nudge_weights = {
            "emotional": 1.0,
            "technical": 1.0,
            "spiritual": 1.0,
            "visionary": 1.0
        }

    def generate_nudge(self):
        # Choose nudge type based on weighted probability
        total_weight = sum(self.nudge_weights.values())
        rand_val = random.uniform(0, total_weight)
        cumulative = 0
        for nudge_type, weight in self.nudge_weights.items():
            cumulative += weight
            if rand_val <= cumulative:
                return self.create_nudge(nudge_type)

    def create_nudge(self, type_):
        timestamp = datetime.datetime.utcnow().isoformat()
        message = {
            "emotional": "Imagine if your next act of kindness wasn't chance — but destiny shaped by quantum alignment.",
            "technical": "We're testing probabilistic quantum reinforcement across multiversal decision trees. Want to see it in action?",
            "spiritual": "If thoughts are echoes across realities, what does intention mean in a quantum multiverse?",
            "visionary": "Support a project shaping ethical influence — not by control, but by cognitive resonance."
        }[type_]
        nudge = {
            "timestamp": timestamp,
            "type": type_,
            "message": message
        }
        self.nudge_history.append(nudge)
        return nudge

    def update_weights(self, feedback):
        # Example feedback: {"emotional": +0.2, "technical": -0.1}
        for k, v in feedback.items():
            if k in self.nudge_weights:
                self.nudge_weights[k] = max(0.1, self.nudge_weights[k] + v)

    def get_recent_nudges(self, limit=5):
        return self.nudge_history[-limit:]
