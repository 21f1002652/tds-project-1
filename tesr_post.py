import requests,os

url = "http://127.0.0.1:8000/api-endpoint"

payload = {
    "secret": os.getenv("USERCODE"),
    "email": "test@example.com",
    "task": "demo-task",
    "round": 2,
    "nonce": "123",
    "brief": "Build a simple HTML page",
    "evaluation_url": "http://example.com/eval",
    "attachments": []
}

resp = requests.post(url, json=payload)
print(resp.status_code)
print(resp.json())
