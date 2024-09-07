import aiohttp
from homeassistant.helpers.entity import Entity

API_URL = 'https://api.planethoster.net/reseller-api/test-connection'

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up PlanetHoster sensors based on a config entry."""
    api_key = config_entry.data.get("api_key")
    api_user = config_entry.data.get("api_user")

    async_add_entities([PlanetHosterTestSensor(), PlanetHosterConnectionTestSensor(api_key, api_user)])

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

    @property
    def name(self):
        """Return the name of the sensor."""
        return "PlanetHosterConnectionTestSensor"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch the connection status from the PlanetHoster API asynchronously."""
        headers = {
            'X-API-KEY': self._api_key,
            'X-API-USER': self._api_user
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(API_URL, headers=headers) as response:
                    if response.status == 200:
                        self._state = "on"
                    else:
                        self._state = "off"
        except aiohttp.ClientError:
            self._state = "off"