from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data[DOMAIN] = PlanetHosterAPI(entry.data["api_key"], entry.data["api_user"])
    hass.config_entries.async_setup_platforms(entry, ["sensor"])
    return True