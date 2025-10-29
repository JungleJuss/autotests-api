import httpx

payload = {
    "email": "user@mail.ru",
    "password": "password"
}

response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
response_data = response.json()['token']['accessToken']

response_with_token = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {response_data}"})
print(response_with_token.json())
print(response_with_token.status_code)