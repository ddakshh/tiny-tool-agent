from tools import get_weather
def run_agent(user_query):
     print("[LOG] Query received")
     query = user_query.lower()
     weather_word = ["weather(", "temp", "temperature", "climate"]
     if any(word in query for word in weather_word):
          words = query.split ()
          ignorewords = [
            "what", "what's", "is", "the",
            "weather", "temp", "temperature",
            "climate", "in", "today"]
          city = None
          for word in words :
               cleanedword = word.strip("?.")
               if cleanedword not in ignorewords:
                    city=cleanedword

          if city :
            print("[LOG] Weather tool selected")
            print(f"[LOG] Extracted city: {city}")

            result = get_weather(city)
            print("[LOG] Weather fetched successfully")
            return result
          return "invalid try again "
     
               