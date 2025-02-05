# Package Managers and Installers
# Package managers help install and manage software dependencies.

# Example: Installing a package with pip

# Run in the terminal, not in Python:
# pip install requests

import requests

print(requests.get("https://www.python.org").status_code)
