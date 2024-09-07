"""PlanetHoster Integration."""
from homeassistant.helpers.entity import Entity

DOMAIN = "planethoster"

def setup(hass, config):
    """Set up the PlanetHoster integration."""
    hass.states.set(f"{DOMAIN}.test_sensor", 100)
    return True