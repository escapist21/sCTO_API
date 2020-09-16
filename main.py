import requests
import requests.auth as auth
import pprint
import json
from datetime import date


class sCTO:

    def __init__(self, server_name, form_id, username, password):
        self.server_name = server_name
        self.form_id = form_id
        self.username = username
        self.password = password

    def construct_url(self):
        url = f'https://{self.server_name}.surveycto.com/api/v2/forms/data/wide/json/{self.form_id}?date=0'
        return url

    def pull_data(self):
        url = self.construct_url()
        try:
            response = requests.get(
                url=url,
                auth=auth.HTTPBasicAuth(username=self.username, password=self.password)
            )
        except Exception as e:
            response = False
            print(e)

        return response

    def get_data(self):
        response = self.pull_data()

        return response.text


def main():
    server_name = str(input('Enter server name: '))
    form_id = str(input('Enter Form ID: '))
    username = str(input('Enter user name: '))
    password = str(input('Enter password: '))

    survey = sCTO(server_name=server_name,
                  form_id=form_id,
                  username=username,
                  password=password)

    data = survey.get_data()
    pprint.pprint(data)
    json_data = json.loads(data)
    today = date.today()
    today_fmt = today.strftime("%d_%m_%Y")
    with open(f"{form_id}_{today_fmt}.json", 'w+') as file:
        json.dump(json_data, file)



if __name__ == '__main__':
    main()