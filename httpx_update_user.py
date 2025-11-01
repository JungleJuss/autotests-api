import httpx
from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "password",
    "lastName": "string",
    "firstName": "Patrick",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}


login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
auth_token = login_response_data['token']['accessToken']
headers = {
        "Authorization": f"Bearer {auth_token}"
    }

update_user = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

update_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", json=update_user, headers=headers)



