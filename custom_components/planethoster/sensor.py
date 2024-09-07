import logging
import aiohttp

_LOGGER = logging.getLogger(__name__)

from homeassistant.helpers.entity import Entity

DOMAIN_LIST_API_URL = 'https://api.planethoster.net/reseller-api/list-domains'
API_URL_STATUS = 'https://api.planethoster.net/reseller-api/domain-status'

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up PlanetHoster sensors based on a config entry."""
    api_key = config_entry.data.get("api_key")
    api_user = config_entry.data.get("api_user")
    
    # Récupérer la liste des domaines
    domains = await fetch_domains(api_key, api_user)

    # Créer des capteurs pour chaque domaine
    sensors = [PlanetHosterDomainSensor(api_key, api_user, domain) for domain in domains]
    async_add_entities(sensors)

async def fetch_domains(api_key, api_user):
    """Fetch the list of domains from the PlanetHoster API."""
    headers = {
        'X-API-KEY': api_key,
        'X-API-USER': api_user
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(DOMAIN_LIST_API_URL, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    _LOGGER.info("Received data from API: %s", data)
                    # Assure-toi que le format correspond
                    return [domain["name"] for domain in data["domains"]]
                else:
                    _LOGGER.error("Error fetching domains: %s", response.status)
                    return []
    except aiohttp.ClientError as e:
        _LOGGER.error("Client error occurred: %s", str(e))
        return []

class PlanetHosterDomainSensor(Entity):
    """Representation of a sensor for a specific domain's redirection status."""

    def __init__(self, api_key, api_user, domain):
        """Initialize the domain redirection sensor."""
        self._state = None
        self._api_key = api_key
        self._api_user = api_user
        self._domain = domain

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"PlanetHoster_{self._domain.replace('.', '_')}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch the redirection status from the PlanetHoster API."""
        headers = {
            'X-API-KEY': self._api_key,
            'X-API-USER': self._api_user
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{API_URL_STATUS}?domain={self._domain}", headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        self._state = "internal" if data["status"] == "internal" else "external"
                    else:
                        self._state = "unknown"
        except aiohttp.ClientError:
            self._state = "error"
