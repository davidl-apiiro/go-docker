import requests

def test_api_key():
    # This is a hypothetical example of how an API key might be included in a test file
    api_key = "abc123XYZ789"  # This is the secret API key
    response = requests.get("https://third-party-api.com/data", headers={"Authorization": f"Bearer {api_key}"})
    
    assert response.status_code == 200
    print("API connection test passed.")

if __name__ == "__main__":
    test_api_key()
