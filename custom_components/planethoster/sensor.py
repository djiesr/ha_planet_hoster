from homeassistant.helpers.entity import Entity

from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the PlanetHoster sensors."""
    api = hass.data[DOMAIN]
    domain_data = await hass.async_add_executor_job(api.get_all_domains)

    sensors = []
    for domain in domain_data:
        sensors.append(PlanetHosterDomainSensor(api, domain))

    async_add_entities(sensors, True)

class PlanetHosterDomainSensor(Entity):
    """Representation of a sensor for a specific domain."""

    def __init__(self, api, domain):
        self.api = api
        self._domain = domain
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"sensor.{self._domain['name'].replace('.', '_')}_id"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._domain['id']

    def update(self):
        """Fetch new state data for the sensor."""
        self._domain = self.api.get_domain_info(self._domain['name'])
        self._state = self._domain['id']
