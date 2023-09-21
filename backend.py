import requests

API_KEY = "7cbdb616deb72a865f0b119668e36446"
def get_data(place, forecast_days= None):
    url = "https://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place = "Tokyo", forecast_days=3))