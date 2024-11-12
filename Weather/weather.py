import requests

api_key = "bd5e378503939ddaee76f12ad7a97608"

while True:
    location = input("Введите название города: ")

    result = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
    )
    if result.json()["cod"] == "404":
        print("Неверное местоположение!")
        continue
    break

temperature = round(result.json()["main"]["temp"])
feels_like = round(result.json()["main"]["feels_like"])

print(f"Погода в городе {location[0].upper()}{location[1:]} {temperature}° C")
print(f"Ощущается как {feels_like}° C.")
