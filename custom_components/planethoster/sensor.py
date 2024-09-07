import logging
from homeassistant.core import HomeAssistant

from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    _LOGGER.debug("Setting up PlanetHoster integration")
    return True

async def async_setup_entry(hass: HomeAssistant, config_entry):
    _LOGGER.debug("Setting up PlanetHoster entry")

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the PlanetHoster sensors."""
    api = hass.data[DOMAIN]
    async_add_entities([PlanetHosterTestSensor(api)], True)

class PlanetHosterTestSensor(Entity):
    """Representation of a PlanetHoster test sensor."""

    def __init__(self, api):
        self._api = api
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return "PlanetHoster Test Connection"
##
    @property
    def state(self):
        """Return the state of the sensor."""
##        return self._state
        return 100

    def update(self):
        """Fetch new state data for the sensor."""
        response = self._api.test_connection()
        self._state = response.get("status", "unknown")

