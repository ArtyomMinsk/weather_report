import requests


class Astronomy:
    key = '4bb11b6a81c6cf11'

    def __init__(self, zipcode):
        self.zipcode = zipcode

    def get_suntimes(self):
        url = 'http://api.wunderground.com/api/' + self.key +\
         '/geolookup/astronomy/q/' + self.zipcode + '.json'

        r = requests.get(url)
        parsed_json = r.json()

        self.sunrise = parsed_json['sun_phase']['sunrise']
        self.sunset = parsed_json['sun_phase']['sunset']

    def __str__(self):
        return "Predicted sunrise and sunset:\n\nSunrise: {}:{}\nSunset: {}:{}\n".format(self.sunrise['hour'], self.sunrise['minute'], self.sunset['hour'], self.sunset['minute'])
