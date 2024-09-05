from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up PlanetHoster integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up PlanetHoster from a config entry."""
    api_key = config_entry.data["api_key"]
    api_user = config_entry.data["api_user"]

    # Initialise l'API avec les informations d'authentification
    hass.data[DOMAIN] = PlanetHosterAPI(api_key, api_user)

    # Configurer la plateforme de capteurs (sensor)
    hass.config_entries.async_setup_platforms(config_entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Unload PlanetHoster config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, ["sensor"])
    if unload_ok:
        hass.data.pop(DOMAIN)
    return unload_ok

import requests

class PlanetHosterAPI:
    def __init__(self, api_key, api_user):
        self.api_key = api_key
        self.api_user = api_user
        self.base_url = "https://your-api-url.com"  # Remplace par l'URL correcte de l'API

    def get_all_domains(self):
        # Exemple de requête pour récupérer les domaines hébergés
        url = f"{self.base_url}/domains"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "API-User": self.api_user
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_domain_info(self, domain):
        # Exemple de requête pour obtenir les informations sur un domaine spécifique
        url = f"{self.base_url}/domains/{domain}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "API-User": self.api_user
        }
        response = requests.get(url, headers=headers)
        return response.json()
