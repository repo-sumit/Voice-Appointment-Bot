import csv
from datetime import datetime

def log_conversation(user_input, response_text):
    with open("data/logs.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), user_input, response_text])
