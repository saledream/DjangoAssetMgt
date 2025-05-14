import requests
from bs4 import BeautifulSoup
from datetime import datetime
from assets.models import WindowUpdateHistory  # Import your model

MICROSOFT_UPDATE_URL = "https://www.catalog.update.microsoft.com/Search.aspx?q=Windows+11+Updates"

def parse_update_data(html_data):

   pass
    
def fetch_microsoft_updates():
    response = requests.get(MICROSOFT_UPDATE_URL)
    if response.status_code != 200:
        print("Failed to fetch updates from Microsoft")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"soup title:{soup.title} ")

    # Extract updates (adjust this part based on actual page structure)
    for link in soup.find_all('tr'):
        print(link)
        print(":<====================================================>:")
       
   
