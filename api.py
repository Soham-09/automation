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

