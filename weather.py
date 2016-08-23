from endpoints.conditions import Conditions
from endpoints.forecast import Forecast
from endpoints.astronomy import Astronomy
from endpoints.alerts import Alerts
from endpoints.hurricanes import Hurricanes


def main():
    while(True):
        # User enters their zipcode on the command line
        zipcode = input('Please enter your zipcode: \n')
        print('=' * 50)

        # Determine the current weather conditions at the given zipcode
        conditions = Conditions(zipcode)
        conditions.get_current_conditions()
        print(conditions)
        print('-' * 20)

        # Determine the 10 day forecast at the given zipcode
        forecast = Forecast(zipcode)
        forecast.get_10day_forecast()
        print('-' * 20)

        # Determine the sunrise and sunset at the given zipcode
        astronomy_forecast = Astronomy(zipcode)
        astronomy_forecast.get_suntimes()
        print(astronomy_forecast)
        print('-' * 20)

        # Determine any weather alerts for the given zipcode
        alerts = Alerts(zipcode)
        alerts.get_alerts()
        print('-' * 20)

        # Determine any active hurricanes
        hurricanes = Hurricanes()
        hurricanes.get_hurricanes()

if __name__ == '__main__':
    main()
