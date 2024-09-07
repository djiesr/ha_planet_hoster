import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

class PlanetHosterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for PlanetHoster."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="PlanetHoster", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("api_key"): cv.string,
                vol.Required("api_user"): cv.string,
            })
        )
