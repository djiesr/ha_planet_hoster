from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN
from .planethoster_api import PlanetHosterAPI

class PlanetHosterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for PlanetHoster."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Valider les informations API
            try:
                api = PlanetHosterAPI(user_input["api_key"], user_input["api_user"])
                await self.hass.async_add_executor_job(api.get_all_domains)
                return self.async_create_entry(title="PlanetHoster", data=user_input)
            except Exception:
                errors["base"] = "cannot_connect"

        # Formulaire pour entrer les clés API
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("api_key"): str,
                vol.Required("api_user"): str,
            }),
            errors=errors
        )
