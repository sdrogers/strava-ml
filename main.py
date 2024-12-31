'''strava_ml code for extracting and performing ml on strava activity data'''
import logging
import configparser
from fastapi import FastAPI
from stravalib.client import Client
from constants import STRAVA_AUTH_URL


# Setup FastAPI
app = FastAPI()

# Setup stravaclient
client = Client()

# Create a logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Read the config
config_parser = configparser.ConfigParser()
config_parser.read("config.ini")
config = config_parser.defaults()
# Debug out the config
for key, value in config.items():
    logger.debug("%s: %s", str(key), str(value))



@app.get("/")
def home():
    return "Hello"


