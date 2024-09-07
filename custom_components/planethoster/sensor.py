"""Sensor for PlanetHoster."""
from homeassistant.helpers.entity import Entity

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the PlanetHoster sensor."""
    add_entities([PlanetHosterTestSensor()])

class PlanetHosterTestSensor(Entity):
    """Representation of a test sensor for PlanetHoster."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = 100

    @property
    def name(self):
        """Return the name of the sensor."""
        return "PlanetHosterTestSensor"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state
