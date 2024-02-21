import json

# Replace 'log.json' with the actual path to your JSON file
file_path = 'log.json'

# Initialize counters
get_count = 0
post_count = 0

# Read the contents of the JSON file
try:
    with open(file_path, 'r') as file:
        json_string = file.read()
        data = json.loads(json_string)
except FileNotFoundError:
    print(f"File '{file_path}' not found")
    # Handle the error appropriately
except json.JSONDecodeError:
    print(f"Invalid JSON format in file '{file_path}'")
    # Handle the error appropriately

# Check if the data is a list or a dictionary
if isinstance(data, list):
    # If it's a list, iterate through each element
    for item in data:
        if isinstance(item, dict) and 'method' in item:
            if item['method'] == 'GET':
                get_count += 1
            elif item['method'] == 'POST':
                post_count += 1


# Print the counts
print(f"Number of GET requests: {get_count}")
print(f"Number of POST requests: {post_count}")
