import logging

import voluptuous as vol

from homeassistant import config_entries, core, data_entry_flow, exceptions

from .const import(
    DOMAIN,
    CONF_USERNAME, 
    CONF_PASSWORD
)


class SomfyProtexiomConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config Flow to configure easily Somfy Protexiom"""
    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            pass # TODO: process info

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({
                vol.Required("CONF_USERNAME"): str,
                vol.Required("CONF_PASSWORD"): str
            })
        )
