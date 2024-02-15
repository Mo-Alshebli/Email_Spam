import requests

# Replace 'http://127.0.0.1:8000' with the actual URL of your FastAPI app
url = 'http://127.0.0.1:8000/predict/'

# Replace this with the actual email text you want to classify
data = {"text": "I want to go to school"}

response = requests.post(url, json=data)

# Print the response from the server
print(response.json())
