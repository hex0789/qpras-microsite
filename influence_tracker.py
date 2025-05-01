
import datetime
import csv
import os

class InfluenceTracker:
    def __init__(self, log_file='convergence_log.csv'):
        self.log_file = log_file
        self.fields = ['timestamp', 'source', 'event_type', 'details']

        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.fields)
                writer.writeheader()

    def log_event(self, source, event_type, details):
        entry = {
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'source': source,
            'event_type': event_type,
            'details': details
        }
        with open(self.log_file, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writerow(entry)
        print(f"[Tracker] Logged event: {entry}")

    def show_log(self):
        with open(self.log_file, mode='r', encoding='utf-8') as f:
            return f.read()
