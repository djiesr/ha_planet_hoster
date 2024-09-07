import requests
from homeassistant.helpers.entity import Entity

API_URL = 'https://api.planethoster.net/reseller-api/test-connection'

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the PlanetHoster sensors."""
    api_key = config.get('api_key')
    api_user = config.get('api_user')
    
    add_entities([PlanetHosterTestSensor(), PlanetHosterConnectionTestSensor(api_key, api_user)])

class PlanetHosterTestSensor(Entity):
    """Representation of a test sensor for PlanetHoster."""

    def __init__(self):
        """Initialize the test sensor."""
        self._state = 100

    @property
    def name(self):
        """Return the name of the sensor."""
        return "PlanetHosterTestSensor"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

class PlanetHosterConnectionTestSensor(Entity):
    """Representation of a sensor testing the PlanetHoster API connection."""

    def __init__(self, api_key, api_user):
        """Initialize the connection test sensor."""
        self._state = "off"
        self._api_key = api_key
        self._api_user = api_user
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return "PlanetHosterConnectionTestSensor"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch the connection status from the PlanetHoster API."""
        try:
            headers = {
                'X-API-KEY': self._api_key,
                'X-API-USER': self._api_user
            }
            response = requests.get(API_URL, headers=headers)

            if response.status_code == 200:
                self._state = "on"
            else:
                self._state = "off"
        except requests.RequestException:
            self._state = "off"
