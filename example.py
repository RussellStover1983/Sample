import requests

def authenticate(username, password):
    auth_url = "https://api.canvasmedical.com/v1/authenticate"
    payload = {"username": username, "password": password}
    response = requests.post(auth_url, json=payload)
    response.raise_for_status()
    return response.json().get('token')

def check_insurance_eligibility(token, patient_id):
    eligibility_url = f"https://api.canvasmedical.com/v1/patients/{patient_id}/insurance/eligibility"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(eligibility_url, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    USERNAME = "your_username"
    PASSWORD = "your_password"
    PATIENT_ID = "12345"

    try:
        token = authenticate(USERNAME, PASSWORD)
        eligibility = check_insurance_eligibility(token, PATIENT_ID)
        print("Eligibility Status:", eligibility.get("status"))
    except requests.HTTPError as err:
        print(f"API request failed: {err}")
