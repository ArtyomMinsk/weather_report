import requests


class Alerts:
    key = '4bb11b6a81c6cf11'

    def __init__(self, zipcode):
        self.zipcode = zipcode

    def get_alerts(self):
        url = 'http://api.wunderground.com/api/' + self.key +\
         '/geolookup/alerts/q/' + self.zipcode + '.json'

        r = requests.get(url)
        parsed_json = r.json()

        print("Current weather alerts:\n\n")
        for alert in parsed_json['alerts']:
            print('Alert Type: {}'.format(alert['type']))
            print('Description: {}'.format(alert['description']))
            print('Issued: {}'.format(alert['date']))
            print('Expires: {}'.format(alert['expires']))
            print('Message: {}'.format(alert['message']))
