import requests

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
# print(json)

description = json.get("weather")[0].get("description")
print("Todays forcast is", description)
temp_min = json.get("main").get("temp_min")
print("The min temperature is", temp_min)
temp_max = json.get("main").get("temp_max")
print("The max temperature is", temp_max)
