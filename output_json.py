import json

text_file_path = 'data.txt'
with open(text_file_path, 'r') as text_file:
    content = text_file.read()
    data = eval(content)

result_dict = {}
for stock_data in data:
    stock_name = stock_data[0]
    json_string = stock_data[1]

    try:
        parsed_data = json.loads(json_string)
        result_dict[stock_name] = parsed_data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON for {stock_name}: {e}")
 
json_output_file_path = 'output.json'
with open(json_output_file_path, 'w') as json_output_file:
    json.dump(result_dict, json_output_file, indent=2)
 
print(f"JSON file created")