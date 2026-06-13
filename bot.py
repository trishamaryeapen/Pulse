# Pulse - Daily summary bot
# Fetches: weather (wttr.in) and quote (zenquotes.io)
# Runs: every day at 8 AM UTC via GitHub Actions

import requests
from datetime import date

def get_weather(city="Thiruvananthapuram"):
    """Fetch today's weather as a one-line text summary."""
    import os

     # This pulls the hidden secret directly from GitHub's secure server environment
    api_key = os.environ.get("WEATHER_API_KEY")

    url = f"https://wttr.in{city}?format=3"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()  # remove trailing newline
    except Exception as e:
        return "Weather unavailable :("

def get_quote():
    """Fetch a random motivational quote from ZenQuotes."""
    # Ensure this URL matches exactly
    url = "https://zenquotes.io"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        quote = data[0]['q']  # Note: zenquotes returns a list, so we need data[0]
        author = data[0]['a']
        return f'"{quote}" - {author}'
    except Exception as e:
        return "Quote unavailable :("
def get_fact():
    """Fetch a random fact from Factretriever"""
    url = "https://www.factretriever.com/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()         # JSON -> Python list
        fact = data[0]['q']
        return f"{fact}" 
    except Exception as e:
        return "Fact unavailable :("

def build_summary():
    """Assemble the full daily summary from all data sources."""
    today = date.today().strftime("%A, %d %b %Y")
    weather = get_weather()
    quote = get_quote()
    
    summary = f"""
PULSE - Daily Summary
{today}
----------------------------------------

WEATHER
{weather}

TODAY'S QUOTE
{quote}

TODAY'S FACT
{fact}
"""
    return summary

def run():
    """Main entry point, called by GitHub Actions."""
    summary = build_summary()
    print(summary)
    
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    print("Pulse ran successfully!")

if __name__ == "__main__":
    run()
