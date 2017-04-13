import os
import subprocess
import time
import datetime
import random
from datetime import datetime, timedelta
from apscheduler.scheduler import Scheduler
from integrations import Slack
import teammates.yaml

# Set the day of the week you want the job to run
# Monday >>> Sunday === 0 >>> 6
set_day_of_week = 0

n_assigned_list = []
assigned_list = []

def time_interval():
    return datetime.datetime.today().weekday(set_day_of_week) + timedelta(days=7)

s = sched.scheduler(time.time, time.sleep)
while True:
    if not s.queue():
        time_next_run = time_interval
        s.enterabs(time_next_run, 1, random_pair, datetime.datetime.today())
    else:
        time.sleep(timedelta(days=7))

def random_pair(date):
    if n_assigned_list > 0:
        pair = []
        while len(pair) < 2:
            p = n_assigned_list.pop()
            pair.append(p)
        else
            # save_assigned(pair, date)
            print pair date
            # Slack.send_message(pair)
    else
        with open("employees.yaml", 'r') as stream:
            data = yaml.load(stream)
            n_assigned_list = data['teamates']
            random.shuffle(n_assigned_list)
        random_pair(date)


def unassigned_list():
    # Returns list of remaining teamates list not yet assigned pair
    print n_assigned_list

def assigned_list():
    # Returns list of teamates list already assigned pair
    print assigned_list

def last_assigned(teamate):
    # query db to get last time teamate was assigned...?

def save_assigned(pair, date):
    # Add DB to save last assigned list...?

# class Teammate(name):
#
#     def __init__(self, email, last_paired):
#             """Return a new teammate object."""
#             self.email = email
#             self.last_paired = last_assigned(self)
