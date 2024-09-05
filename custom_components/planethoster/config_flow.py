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
        
        if user_input is not None:
            # Si tout est correct, on crée une entrée
            return self.async_create_entry(title="PlanetHoster", data=user_input)

        # Formulaire pour entrer les clés API
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("api_key"): str,
                vol.Required("api_user"): str,
            }),
            errors=errors
        )
    
async def async_step_user(self, user_input=None):
    """Handle the initial step."""
    errors = {}
    
    if user_input is not None:
        # Valider les informations API en envoyant une requête
        try:
            api = PlanetHosterAPI(user_input["api_key"], user_input["api_user"])
            await hass.async_add_executor_job(api.get_all_domains)  # Vérifie si l'API répond
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