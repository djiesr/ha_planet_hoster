import requests

class PlanetHosterAPI:
    """Class to interact with PlanetHoster API."""

    def __init__(self, api_key, api_user):
        self.api_key = api_key
        self.api_user = api_user
        self.base_url = "https://api.planethoster.net/reseller-api"

    def test_connection(self):
        """Test the connection to the PlanetHoster API."""
        url = f"{self.base_url}/test-connection"
        headers = {
            "X-API-KEY": self.api_key,
            "X-API-USER": self.api_user
        }
        response = requests.get(url, headers=headers)
        return response.json()
