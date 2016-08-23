import requests


class Forecast:
    key = '4bb11b6a81c6cf11'

    def __init__(self, zipcode):
        self.zipcode = zipcode

    def get_10day_forecast(self):
        url = 'http://api.wunderground.com/api/' + self.key +\
         '/geolookup/forecast10day/q/' + self.zipcode + '.json'

        r = requests.get(url)
        parsed_json = r.json()

        print("10 day weather forcast for {}, {}:\n".format(parsed_json['location']['city'], parsed_json['location']['state']))

        for day in parsed_json['forecast']['simpleforecast']['forecastday']:
            print(day['date']['weekday'] + ' (' + day['date']['pretty'] + '):')
            print('  Conditions: ' + day['conditions'])
            print('  High:' + day['high']['fahrenheit'] + 'F')
            print('  Low: ' + day['low']['fahrenheit'] + 'F')
        print()
