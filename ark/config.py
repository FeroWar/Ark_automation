import configparser

# Create a ConfigParser instance
config = configparser.ConfigParser()
config.read("config.ini")  # Load the config file

# Read values from the SETTINGS section
INVENTORY_OPEN_INTERVAL = float(config["SETTINGS"].get("INVENTORY_OPEN_INTERVAL", 5))
INVENTORY_CLOSE_INTERVAL = float(config["SETTINGS"].get("INVENTORY_CLOSE_INTERVAL", 5))
TIMER_FACTOR = float(config["SETTINGS"].get("TIMER_FACTOR", 1))
ARK_PATH = config["SETTINGS"].get("ARK_PATH")
