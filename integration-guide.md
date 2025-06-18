# Integrating with Canvas Medical’s Patient Insurance Eligibility API

## Introduction

This guide walks you through how to integrate with Canvas Medical’s API to check a patient’s insurance eligibility in real time. It covers authentication, making API calls, handling responses, and error management. You can use this guide to build internal tools, automate workflows, or simply explore Canvas Medical’s API as part of a technical evaluation.

---

## Prerequisites

Before you begin, ensure you have the following:

- A valid Canvas Medical API username and password.
- Python 3.x installed on your system.
- The `requests` library installed (`pip install requests`).
- Basic knowledge of REST APIs and JSON.
- Access to a terminal or command line interface.
- *(Optional but recommended)* An API testing tool like:
  - [**Bruno**](https://www.usebruno.com/) – open source, local-first API client.
  - [**Postman**](https://www.postman.com/) – cloud-based collaboration platform.
  - [**Insomnia**](https://insomnia.rest/) – lightweight REST/GraphQL tool.

> These tools let you test authentication, send requests, and inspect responses visually before integrating in code. Perfect for prototyping or debugging.

---

## Step 1: Authenticate and Obtain an Access Token

Canvas Medical’s API uses token-based authentication. You send a `POST` request with your credentials to retrieve a JSON Web Token (JWT). This token is used in the `Authorization` header for all subsequent API requests.

**Python Example:**

```python
import requests

auth_url = "https://api.canvasmedical.com/v1/authenticate"
payload = {
    "username": "your_username",
    "password": "your_password"
}

response = requests.post(auth_url, json=payload)
response.raise_for_status()  # Raises an error if the response is unsuccessful
token = response.json().get('token')
print(f"Authentication token: {token}")

```

---
## Step 2: Check Patient Insurance Eligibility
With a valid token, you can now query the patient insurance eligibility endpoint.

API Endpoint Format:

```bash

GET https://api.canvasmedical.com/v1/patients/{patient_id}/insurance/eligibility

```

Python Example:

```python

headers = {"Authorization": f"Bearer {token}"}
patient_id = "12345"

eligibility_url = f"https://api.canvasmedical.com/v1/patients/{patient_id}/insurance/eligibility"
response = requests.get(eligibility_url, headers=headers)

if response.status_code == 200:
    eligibility_data = response.json()
    print("Eligibility Status:", eligibility_data.get("status"))
else:
    print("Failed to retrieve eligibility data:", response.status_code)
```

Replace 12345 with the actual patient ID you wish to query.

---
## Step 3: Handling the Response

If the request is successful, the API will return a JSON response with the patient’s insurance details. Key fields may include:
- `status` : `"active"`, `"inactive"`, or `"unknown"`
- `coverage_start_date`: Date coverage began
- `coverage_end_date`: Date coverage ends (or null if ongoing)
- `payer`: Name of the insurance provider

You can use this information to:
- Display real-time insurance status to front office staff.
- Trigger alerts or workflows when coverage is missing or inactive.
- Store insurance metadata for reporting or analytics.

---
## Step 4: Error Handling

Always implement error handling to manage API response failures gracefully.

**Common HTTP Errors:**

| Code | Meaning             | Recommendation                                   |
|------|---------------------|--------------------------------------------------|
| 401  | Unauthorized         | Re-authenticate; check credentials/token        |
| 404  | Not Found            | Patient ID may be invalid                       |
| 500  | Internal Server Error| Retry later or contact Canvas support           |

**Python Tip:**

```python
try:
    response.raise_for_status()
except requests.HTTPError as err:
    print(f"Request failed: {err}")

```
---
## Next Steps
Explore other Canvas Medical API endpoints (e.g., appointments, clinical notes).

Integrate the eligibility check into your EHR, intake system, or patient portal.

Automate daily eligibility audits to reduce claim denials.

Build a UI using this endpoint to streamline front desk workflows.

📚 For more information, visit the [**Canvas Medical Development Docs**](https://docs.canvasmedical.com/)
