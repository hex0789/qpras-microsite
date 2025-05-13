import random
from datetime import datetime, timedelta
import pandas as pd


# Define high-net-worth individuals and their basic profiles
HNWI_LIST = [
    {"name": "Elon Musk", "net_worth": 230_000_000_000, "interests": ["technology", "space", "philanthropy"]},
    {"name": "Jeff Bezos", "net_worth": 180_000_000_000, "interests": ["space", "books", "innovation"]},
    {"name": "Warren Buffett", "net_worth": 120_000_000_000, "interests": ["finance", "philanthropy", "legacy"]},
    {"name": "Oprah Winfrey", "net_worth": 2_500_000_000, "interests": ["media", "education", "mental health"]},
    {"name": "MacKenzie Scott", "net_worth": 30_000_000_000, "interests": ["education", "gender equality", "philanthropy"]},
]

# Generate influence profile for each individual
def generate_influence_profile(hnwi):
    return {
        "name": hnwi["name"],
        "net_worth": hnwi["net_worth"],
        "trigger": random.choice(["legacy", "altruism", "spiritual alignment", "AI inspiration"]),
        "medium": random.choice(["viral content", "dream", "AI recommendation", "foundation initiative"]),
        "influence_time": datetime.now() + timedelta(days=random.randint(1, 365)),
        "predicted_donation": round(random.uniform(0.01, 0.1) * hnwi["net_worth"], -6),
        "probability_of_success": round(random.uniform(0.6, 0.98), 2)
    }

# Apply social reinforcement based on simulated influence
def reinforce_profiles(profiles):
    reinforced = []
    for profile in profiles:
        updated = profile.copy()
        boost = 0.0
        if profile["name"] != "Elon Musk" and any(p["name"] == "Elon Musk" and p["probability_of_success"] > 0.85 for p in profiles):
            boost += 0.03
        if profile["name"] != "Warren Buffett" and any(p["name"] == "Warren Buffett" and p["probability_of_success"] > 0.85 for p in profiles):
            boost += 0.02
        updated["probability_of_success"] = min(0.99, updated["probability_of_success"] + boost)
        updated["predicted_donation"] = round(updated["predicted_donation"] * (1 + boost * 2), -6)
        reinforced.append(updated)
    return reinforced

# Main simulation function
def simulate_hyperdonor_campaign():
    profiles = [generate_influence_profile(h) for h in HNWI_LIST]
    reinforced = reinforce_profiles(profiles)
    df = pd.DataFrame(reinforced)
    
    # Sum the total donations of those with a probability of success higher than 0.85
    total_donations = sum(p["predicted_donation"] for p in reinforced if p["probability_of_success"] > 0.85)
    
    # Adding more context for the user:
    print("Hyperdonor Campaign Simulation Results:")
    print(df[["name", "predicted_donation", "probability_of_success"]])
    print(f"Total Donations (with >85% probability): ${total_donations:,.2f}")

    return df, total_donations

if __name__ == "__main__":
    df, total = simulate_hyperdonor_campaign()
    print("Projected Donations Over 85% Confidence Threshold:")
    print(df[df['probability_of_success'] > 0.85][['name', 'predicted_donation', 'probability_of_success']])
    print(f"Total Projected Donations: ${total:,.2f}")
