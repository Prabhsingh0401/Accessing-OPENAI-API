import requests

URL = "https://api.openai.com/v1/chat/completions"

# This is the payload which we are going to send it to the completion end point.

payload = {
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content": f"What is the first computer in the world?"}],
"temperature" : 1.0,  # More the temperature more the chat Model is Creative.
"top_p":1.0,
"n" : 1,
"stream": False,     #To get the prompt in stream set the value to True.
"presence_penalty":0,
"frequency_penalty":0,
}

# Set your api key here in header for the authentication.

headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {openai.api_key}"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)