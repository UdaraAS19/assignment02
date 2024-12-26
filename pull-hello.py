import requests

# URL of the raw content of the file
url = "https://raw.githubusercontent.com/UdaraAS19/assignment02/refs/heads/main/hello.py"

response = requests.get(url)
if response.status_code == 200:
    with open("downloaded_hello.py", "w") as file:
        file.write(response.text)
    print("Script downloaded successfully.")
else:
    print("Failed to fetch the script. Status code:", response.status_code)
