from homeassistant.helpers.entity import Entity

DOMAIN = "planethoster"

async def async_setup_entry(hass, config_entry, async_add_entities):
    # Simuler la récupération de la liste des domaines à partir de l'API
    api = hass.data[DOMAIN]
    domain_data = await api.get_all_domains()

    sensors = []
    for domain in domain_data:
        sensors.append(PlanetHosterDomainSensor(api, domain))

    async_add_entities(sensors, True)

class PlanetHosterDomainSensor(Entity):
    def __init__(self, api, domain):
        self.api = api
        self._domain = domain
        self._state = None

    @property
    def name(self):
        return f"sensor.{self._domain['name'].replace('.', '_')}_id"

    @property
    def state(self):
        return self._domain['id']

    def update(self):
        # Requêter l'API pour obtenir l'ID du domaine (ou d'autres informations)
        self._domain = self.api.get_domain_info(self._domain['name'])
        self._state = self._domain['id']