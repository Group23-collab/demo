import csv
import json
from datetime import datetime

json_file_path = 'output.json'
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)
 
csv_file_path = 'output.csv'
 
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["Stock name", "Date", "Price"])

    for stock_name, stock_data in json_data.items():
        for date_str, price in stock_data.items():
            date_only = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d T%H:%M:%S")
            csv_writer.writerow([stock_name, date_only, price])
 
print(f"CSV file is created")