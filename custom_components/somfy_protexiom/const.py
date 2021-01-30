"""Constants for integration_blueprint."""
# Base component constants
NAME = "Somfy Protexiom"
DOMAIN = "somfy_protexiom"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.1"


# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
-------------------------------------------------------------------
"""