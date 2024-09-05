import requests

class PlanetHosterAPI:
    """Class to interact with PlanetHoster API."""

    def __init__(self, api_key, api_user):
        self.api_key = api_key
        self.api_user = api_user
        self.base_url = "https://your-api-url.com"  # Replace with actual URL

    def get_all_domains(self):
        """Get all domains hosted on the account."""
        url = f"{self.base_url}/domains"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "API-User": self.api_user
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_domain_info(self, domain):
        """Get specific domain information."""
        url = f"{self.base_url}/domains/{domain}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "API-User": self.api_user
        }
        response = requests.get(url, headers=headers)
        return response.json()
