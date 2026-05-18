import requests
import os 
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("WEATHER_API_KEY")
def get_weather (city : str) :
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
   

    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"{city} : {temp}c, {weather}"
    else :
        return "error  city invald"
        