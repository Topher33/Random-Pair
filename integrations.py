import requests
import json

class Slack(pairs_list):

    slack_url = '<some slack hook url>'
    j_template = 'Pair for this week is #{teammate_1} and #{teammate_2}'

    def send_message(pairs_list)
    teammate_1 = pairs_list[0]
    teammate_2 = pairs_list[1]
    j_data = j_template
    r = requests.post(slack_url, data = j_data)
