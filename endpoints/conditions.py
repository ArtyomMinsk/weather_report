import requests


class Conditions:

    key = '4bb11b6a81c6cf11'

    def __init__(self, zipcode):
        self.zipcode = zipcode

    def get_current_conditions(self):
        url = 'http://api.wunderground.com/api/' + self.key +\
         '/geolookup/conditions/q/' + self.zipcode + '.json'

        r = requests.get(url)
        parsed_json = r.json()

        self.city = parsed_json['location']['city']
        self.state = parsed_json['location']['state']
        self.weather = parsed_json['current_observation']['weather']
        self.temperature_string = parsed_json['current_observation']['temperature_string']
        self.feelslike_string = parsed_json['current_observation']['feelslike_string']
        self.relative_humidity = parsed_json['current_observation']['relative_humidity']

    def __str__(self):
        return "Current weather in {}, {}:\n\n {}\n Temperature: {}\n Feels like: {}\n Humidity: {}\n".format(self.city, self.state, self.weather, self.temperature_string, self.feelslike_string, self.relative_humidity)
