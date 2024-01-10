//post json call
import requests
import json

# Replace with your actual endpoint and headers
endpoint = 'https://api.example.com/post'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}

# Replace 'your_file.json' with the actual file path
file_path = 'your_file.json'

try:
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Make a simulated HTTP POST request to the endpoint
    response = requests.post(endpoint, headers=headers, json=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Print the response
        print("Response:", response_data)

    else:
        print("Error: Request failed with status code", response.status_code)

except FileNotFoundError:
    print("Error: File not found")

except json.JSONDecodeError:
    print("Error: Invalid JSON format in the file")

except requests.RequestException as e:
    print("Error:", e)

//get json call
import requests
import json

# Replace with your actual endpoint and headers
endpoint = 'https://api.example.com/data'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}

try:
    # Make a simulated HTTP GET request to the endpoint
    response = requests.get(endpoint, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Print the response
        print("Response:", data)

    else:
        print("Error: Request failed with status code", response.status_code)

except requests.RequestException as e:
    print("Error:", e)
//json format
{
  "entries": [
    {
      "service": "service1",
      "operation": "operation1",
      "endpoint": "/api/endpoint1"
    },
    {
      "service": "service2",
      "operation": "operation2",
      "endpoint": "/api/endpoint2"
    }
  ]
}
//json parsing
import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    # Specify the path to your JSON file
    json_file_path = 'input.json'

    # Read data from the JSON file
    json_data = read_json_file(json_file_path)

    # Get the list of entries from the JSON data
    entries_list = json_data.get('entries', [])

    # Create a dictionary to store the information
    result_dict = {}

    # Populate the result dictionary for each entry
    for entry in entries_list:
        service_name = entry.get('service', '')
        operation_name = entry.get('operation', '')
        endpoint = entry.get('endpoint', '')

        # Create a unique key for each entry based on service and operation
        key = f"{service_name}_{operation_name}"

        # Populate the result dictionary
        result_dict[key] = {
            'service': service_name,
            'operation': operation_name,
            'endpoint': endpoint
        }

    # Print the result dictionary
    print("Result Dictionary:", result_dict)

if __name__ == "__main__":
    main()

