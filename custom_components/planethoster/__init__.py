from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN  # Importer le domaine depuis const.py

async def async_setup_entry(hass, config_entry):
    # Utiliser DOMAIN pour stocker les données
    hass.data[DOMAIN] = PlanetHosterAPI(config_entry.data["api_key"], config_entry.data["api_user"])
    hass.config_entries.async_setup_platforms(config_entry, ["sensor"])
    return True