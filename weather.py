import requests


def get_weather_desc_and_temp():
    api_key = "e945998b15f9c864b432b026a1255bc3"
    city = "Orlando"
    url = (
        "http://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&appid="
        + api_key
        + "&units=imperial"
    )

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {"description": description, "temp_min": temp_min, "temp_max": temp_max}


def main():
    weataher_dict = get_weather_desc_and_temp()
    # print(json)
    print("Todays forcast is", weataher_dict.get("description"))
    print("The min temperature is", weataher_dict.get("temp_min"))
    print("The max temperature is", weataher_dict.get("temp_max"))


main()
