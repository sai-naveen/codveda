import requests
city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temp = data["current_condition"][0]["temp_C"]
        weather = data["current_condition"][0]["weatherDesc"][0]["value"]
        humidity = data["current_condition"][0]["humidity"]

        print("\nWeather Information")
        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Condition:", weather)
        print("Humidity:", humidity, "%")

    else:
        print("Error: Unable to fetch data from API")

except requests.exceptions.RequestException:
    print("Error: Network problem or invalid request")