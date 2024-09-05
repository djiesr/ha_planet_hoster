from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN

class PlanetHosterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for PlanetHoster."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL
    
async def async_step_user(self, user_input=None):
    """Handle the initial step."""
    errors = {}
    
    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="PlanetHoster", data=user_input)

        # Formulaire pour entrer les clés API
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("api_key"): str,
                vol.Required("api_user"): str,
            })
        )