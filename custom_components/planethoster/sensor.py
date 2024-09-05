from homeassistant.helpers.entity import Entity

class PlanetHosterDomainSensor(Entity):
    def __init__(self, api):
        self.api = api
        self._state = None

    @property
    def name(self):
        return "PlanetHoster Domain Status"

    @property
    def state(self):
        return self._state

    def update(self):
        domain_info = self.api.get_domain_info('example.com')
        self._state = domain_info.get('status')