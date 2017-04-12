import requests
import json

class Slack(pairs_list):
    j_data = (pairs_list)
    slack_url = '<some slack hook url>'
    r = requests.post(slack_url, data = j_data)
