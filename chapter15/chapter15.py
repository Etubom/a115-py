import requests


def get_current_london_weather():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": 51.507, "longitude": 0.127, "current_weather": True},
    )
    if response.ok:
        return response.json()


def main():
    print(get_current_london_weather())


if __name__ == "__main__":
    main()
