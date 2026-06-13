# Pulse - Daily summary bot
# Fetches: weather (wttr.in) and quote (zenquotes.io)
# Runs: every day at 8 AM UTC via GitHub Actions

import requests
from datetime import date
def get_weather(city="Thiruvananthapuram"):
    """Fetch today's weather as a one-line text summary."""
    url = f"https://wttr.in{city}?format=3"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()  # remove trailing newline
    except Exception as e:
        return "Weather unavailable :("
def get_quote():
    """Fetch a random motivational quote from ZenQuotes."""
    url = "https://zenquotes.io"

