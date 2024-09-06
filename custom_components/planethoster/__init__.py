from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .planethoster_api import PlanetHosterAPI
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the PlanetHoster integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up PlanetHoster from a config entry."""
    api_key = config_entry.data["api_key"]
    api_user = config_entry.data["api_user"]

    # Initialise l'API avec les informations d'authentification
    hass.data[DOMAIN] = PlanetHosterAPI(api_key, api_user)

    # Configurer la plateforme de capteurs
    hass.config_entries.async_setup_platforms(config_entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, ["sensor"])
    if unload_ok:
        hass.data[DOMAIN].pop(config_entry.entry_id)
    return unload_ok
