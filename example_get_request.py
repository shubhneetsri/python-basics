"""
Write a Python function that performs a 
GET request to https://api.vatcomply.com/rates using the requests library.
Include a timeout of 10 seconds.
"""
import requests

def get_exchange_rates():
    url = "https://api.vatcomply.com/rates"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an exception for 4xx/5xx responses
        return response.json()
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None