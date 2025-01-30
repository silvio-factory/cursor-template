# scripts/test_connection.py

# This script tests the internet connection by attempting to connect to GitHub.
# It also displays the current proxy settings being used.
# Useful for debugging connection issues during development and deployment.

import requests

# Create a test script
def test_connection():
    try:
        # Try to connect to GitHub
        response = requests.get('https://github.com', timeout=5)
        print(f"Connection successful! Status code: {response.status_code}")
        
        # Print current proxy settings
        print("\nProxy Settings:")
        print(f"HTTP Proxy: {requests.utils.getproxies().get('http', 'Not set')}")
        print(f"HTTPS Proxy: {requests.utils.getproxies().get('https', 'Not set')}")
        
    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")

if __name__ == '__main__':
    test_connection() 