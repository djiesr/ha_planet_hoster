async def async_setup_entry(hass, config_entry, async_add_entities):
    api_key = config_entry.data["api_key"]
    api_user = config_entry.data["api_user"]

    hass.data[DOMAIN] = PlanetHosterAPI(api_key, api_user)

    # Continuer avec l'ajout de capteurs...