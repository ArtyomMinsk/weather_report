import requests


class Hurricanes:
    key = '4bb11b6a81c6cf11'

    def get_hurricanes(self):
        url = 'http://api.wunderground.com/api/' + self.key +\
            '/currenthurricane/view.json'

        r = requests.get(url)
        parsed_json = r.json()

        print("Current active hurricanes:\n\n")
        for hurricane in parsed_json['currenthurricane']:
            print('Storm Name: {}'.format(hurricane['stormInfo']['stormName']))
            print('Category: {}'.format(hurricane['Current']['Category']))
        print()
