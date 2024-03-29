.popup {
  display: none;
  position: absolute;
  width: 33.33%; /* 1/3 of the original window width */
  height: 33.33vh; /* 1/3 of the original window height */
  top: 33.33%; /* Center vertically */
  left: 33.33%; /* Center horizontally */
  background-color: #fff;
  border: 1px solid #000;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.popup-content {
  padding: 20px;
}




<div id="services-list">
    <div class="service">
        <span>Service 1</span>
        <button class="detail-button" onclick="showDetailModal(1)">Details</button>
    </div>
    <div class="service">
        <span>Service 2</span>
        <button class="detail-button" onclick="showDetailModal(2)">Details</button>
    </div>
    <!-- Add more services dynamically as needed -->
</div>

<!-- Modal -->
<div id="detail-modal" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeDetailModal()">&times;</span>
        <h2>Response Details</h2>
        <p id="response-details"></p>
        <button onclick="downloadResponse()">Download</button>
    </div>
</div>

<script>
    // Function to show modal and load details
    function showDetailModal(serviceId) {
        var modal = document.getElementById("detail-modal");
        var responseDetails = "Response details for Service " + serviceId + ": <br>Mock data goes here.";

        document.getElementById("response-details").innerHTML = responseDetails;
        modal.style.display = "block";
    }

    // Function to close modal
    function closeDetailModal() {
        var modal = document.getElementById("detail-modal");
        modal.style.display = "none";
    }

    // Function to simulate downloading response
    function downloadResponse() {
        // Simulate downloading the response data
        alert("Downloading response...");
    }

    // Close modal when clicking outside of it
    window.onclick = function(event) {
        var modal = document.getElementById("detail-modal");
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
</script>


#include "lrs.h"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pass Count Table</title>
</head>
<body>
    <h1>Pass Count Table</h1>
    <table border="1" id="passCountTable">
        <thead>
            <tr>
                <th>Service Name</th>
                <th>Pass Count</th>
            </tr>
        </thead>
        <tbody id="passCountTableBody">
            <!-- Pass count rows will be dynamically added here -->
        </tbody>
    </table>

    <button id="submitButton">Submit</button>

    <script>
        document.getElementById("submitButton").addEventListener("click", function() {
            fetch("/get_pass_counts")
            .then(response => response.json())
            .then(data => {
                // Clear previous data
                document.getElementById("passCountTableBody").innerHTML = "";
                // Populate table with pass counts
                data.forEach(item => {
                    const serviceName = item.serviceName;
                    const passCount = item.passCount;
                    const row = document.createElement("tr");
                    const serviceNameCell = document.createElement("td");
                    serviceNameCell.textContent = serviceName;
                    const passCountCell = document.createElement("td");
                    passCountCell.textContent = passCount;
                    row.appendChild(serviceNameCell);
                    row.appendChild(passCountCell);
                    document.getElementById("passCountTableBody").appendChild(row);
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>



Action()
{
    // Connect to Virtual Table Server (VTS)
    lrvtc_connect("vts_server_name", 8888, "vts_dataset_name", LR_AUTO);

    // Retrieve data from VTS for account number and account type
    lrvtc_retrieve_row("vts_query_name", "account_number", LR_LAST);
    lrvtc_retrieve_row("vts_query_name", "account_type", LR_LAST);

    // Get the values of account number and account type
    char* accountNumber = lrvtc_get_value("account_number");
    char* accountType = lrvtc_get_value("account_type");

    // Generate claim ID (example: using timestamp)
    char claimId[20];
    sprintf(claimId, "CLAIM_%ld", time(NULL));

    // Print account details and generated claim ID
    lr_output_message("Account Number: %s", accountNumber);
    lr_output_message("Account Type: %s", accountType);
    lr_output_message("Generated Claim ID: %s", claimId);

    // Store claim ID back into VTS for future use
    lrvtc_store_value("claim_id", claimId);

    // Disconnect from VTS
    lrvtc_disconnect();

    return 0;
}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebService Tester</title>
</head>
<body>
    <form action="/execute" method="post">
        <table border="1">
            <tr>
                <th>Select</th>
                <th>Service Name</th>
                <th>Status</th>
                <th>Description</th>
                <th>Details</th>
            </tr>
            {% for service_name in service_names %}
            <tr>
                <td><input type="checkbox" name="selected_services" value="{{ service_name }}"></td>
                <td>{{ service_name }}</td>
                <td><img src="{{ url_for('static', filename='green_icon.png') }}" alt="PASS"></td>
                <td>{{ config['webServices'][loop.index0]['useCase'] }}</td>
                <td><button type="button" onclick="showDetails('{{ service_name }}')">Details</button></td>
            </tr>
            {% endfor %}
        </table>

        <div>
            <label>Iteration Counter: </label>
            <input type="text" name="iteration_counter">
        </div>

        <div>
            <button type="submit">Submit</button>
            <button type="reset">Reset</button>
        </div>
    </form>

    <script>
        function showDetails(serviceName) {
            // Implement logic to show details in a popup
            alert('Details for ' + serviceName);
        }
    </script>
</body>
</html>
///////////////
Action()
{
    // Define your parameter containing the number
    char *parameter = "{your_parameter_name}";

    // Get the length of the parameter
    int length = strlen(parameter);

    // Check if the length is less than 13
    if (length < 13) {
        // Calculate the number of zeros to add
        int zeros_to_add = 13 - length;

        // Create a new string to store the modified parameter
        char modified_parameter[20]; // Assuming a maximum length of 20 for the modified parameter

        // Add zeros to the beginning of the parameter
        for (int i = 0; i < zeros_to_add; i++) {
            modified_parameter[i] = '0';
        }

        // Copy the original parameter to the modified parameter after the added zeros
        strncpy(modified_parameter + zeros_to_add, parameter, length + 1);

        // Update the parameter with the modified value
        lr_save_string(modified_parameter, "modified_parameter");

        // Print the modified parameter for verification
        lr_output_message("Modified Parameter: %s", modified_parameter);
    } else {
        // If the length is already 13 or more, no need to modify
        lr_output_message("Parameter already has 13 or more digits.");
    }

    return 0;
}
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

