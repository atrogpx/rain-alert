import requests
import smtplib

api_key = "ffb96a33df88f6d5574c7648d119282f"

weather_params = {
    "lat": 50.907700,
    "lon": 34.798100,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()


def send_alert():
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = "atiogpx@gmail.com"
    EMAIL_HOST_PASSWORD = "bbcugholbrzhlrdx"

    connection = smtplib.SMTP(EMAIL_HOST)
    connection.starttls()
    connection.login(user=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD)
    connection.sendmail(from_addr=EMAIL_HOST_USER,
                        to_addrs="atrogpx@yahoo.com",
                        msg="Subject: Rain Alert\n\nBring an Umbrella.")


will_rain = False
weather_12hour_list = weather_data["hourly"][0:12]
for _ in weather_12hour_list:
    print(_["weather"][0]["id"])
    if _["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    send_alert()
