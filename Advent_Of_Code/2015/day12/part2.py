import json
def sum_numbers(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_numbers(item) for item in data)
    elif isinstance(data, dict):
        # Check if any property has the value "red" and ignore the entire structure
        if "red" in data.values():
            return 0
        return sum(sum_numbers(value) for value in data.values())
    else:
        return 0


json_file_path = "input.txt"

with open(json_file_path, 'r') as file:
    json_data = json.load(file)

    result = sum_numbers(json_data)

    print("Sum of all numbers in the document:", result)

