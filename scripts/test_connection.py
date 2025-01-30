# scripts/test_connection.py

# This script tests the internet connection by attempting to connect to GitHub.
# It also displays the current proxy settings being used and configures git accordingly.
# Useful for setting the git config before syncing with github issues during development and deployment.

import requests
import subprocess
import sys

def run_git_command(command):
    """Execute a git command and handle potential errors"""
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Successfully executed: {' '.join(command)}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
        print(f"Error output: {e.stderr}")

def configure_git_proxy(proxy_settings):
    """Configure git proxy settings based on the provided dictionary"""
    if not proxy_settings:
        # If no proxy is needed, unset any existing proxy configurations
        run_git_command(['git', 'config', '--global', '--unset', 'http.proxy'])
        run_git_command(['git', 'config', '--global', '--unset', 'https.proxy'])
        print("Git proxy settings cleared - direct connection will be used")
        return

    # Set HTTP proxy
    if 'http' in proxy_settings:
        run_git_command(['git', 'config', '--global', 'http.proxy', proxy_settings['http']])
    
    # Set HTTPS proxy
    if 'https' in proxy_settings:
        run_git_command(['git', 'config', '--global', 'https.proxy', proxy_settings['https']])

def test_connection():
    """Test connection to GitHub and configure git proxy settings accordingly"""
    try:
        # Get current proxy settings
        proxy_settings = requests.utils.getproxies()
        
        # Try to connect to GitHub
        response = requests.get('https://github.com', timeout=5)
        print(f"Connection successful! Status code: {response.status_code}")
        
        # Print current proxy settings
        print("\nDetected Proxy Settings:")
        print(f"HTTP Proxy: {proxy_settings.get('http', 'Not set')}")
        print(f"HTTPS Proxy: {proxy_settings.get('https', 'Not set')}")
        
        # Configure git based on successful connection
        print("\nConfiguring git settings...")
        configure_git_proxy(proxy_settings)
        
        # Verify git configuration
        print("\nCurrent git configuration:")
        run_git_command(['git', 'config', '--global', '--get', 'http.proxy'])
        run_git_command(['git', 'config', '--global', '--get', 'https.proxy'])
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == '__main__':
    success = test_connection()
    sys.exit(0 if success else 1) 