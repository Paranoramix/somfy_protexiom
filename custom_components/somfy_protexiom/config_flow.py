import logging

import voluptuous as vol

from homeassistant import config_entries, core, data_entry_flow, exceptions
from homeassistant.const import DOMAIN, CONF_ENABLED, CONF_USERNAME, CONF_PASSWORD
from homeassistant.core import callback



class SomfyProtexiomConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config Flow to configure easily Somfy Protexiom"""
    async def async_step_user(self, info):
        if info is not None:
            self.data = info
            pass # TODO: process info

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({
                vol.Required("CONF_USERNAME"): str,
                vol.Required("CONF_PASSWORD"): str,
                vol.Required("CONF_ENABLED"): bool
            })
        )