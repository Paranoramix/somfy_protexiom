from homeassistant import config_entries
from .const import DOMAIN

class SomfyProtexiomConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config Flow to configure easily Somfy Protexiom"""
    async def async_step_user(self, info):
        if info is not None:
            pass # TODO: process info

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({vol.Required("password"): str})
        )