from requests import * 


api_key = "cd54318755338c402a7effa01c9cb1e3"



def weather(city):
    response = get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    if response.status_code == 200:
        response = response.json()
        result = {"City" : response["name"],"main" : f"{response["weather"][0]["main"]}", "description" : f"{response["weather"][0]["description"]}", "Temperature" : f"{response["main"]["temp"]}°C", "Feels like" : 
                str(response["main"]["feels_like"]) + "°C", "pressure" : str(response["main"]["pressure"]) + "hPa", "humidity" : response["main"]["humidity"],"visibility" : response["visibility"],
                "wind" : f"{response["wind"]["speed"]} m/s SW "}
        return result
    return "error"
        

def icon(description = "fewclouds"):
    if "few" in description and "clouds" in description:
        return 'image/few_clouds.svg'
    elif "scattered" in description and "clouds" in description:
        return 'image/cloud.svg'
    elif ("broken" in description or "overcast" in description) and "clouds" in description:
        return 'image/clouds.svg'
    elif "shower" in description and "rain" in description:
        return 'image/rain.svg'
    elif "rain" in description:
        return 'image/rainsun.svg'
    elif "thunderstorm" in description:
        return 'image/thunder.svg'
    elif "snow" in description:
        return 'image/snow.svg'
    elif "mist" in description:
        return 'image/mist.svg'
    else:
        return 'image/sun.svg'
    



