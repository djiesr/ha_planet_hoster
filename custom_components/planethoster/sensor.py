from homeassistant.helpers.entity import Entity

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the PlanetHoster sensors."""
    async_add_entities([PlanetHosterTestSensor()], True)

class PlanetHosterTestSensor(Entity):
    """Representation of a static test sensor for PlanetHoster."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return "sensor.planethoster_check"

    @property
    def state(self):
        """Return the state of the sensor."""
        return 100
