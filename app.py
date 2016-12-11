from urllib.request import Request
from urllib.parse import urljoin

CHANNEL_ID = "257441384355725316"

BASE_URL = "https://discordapp.com/api"

req = Request(urljoin(BASE_URL, "channels", CHANNEL_ID, "messages"))
