#!python 
import os
import re
import sys
import requests
import datetime
import json

f= open("_posts/2019-11-13-stevespicksweek11.md","w+")
r = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl", verify=False).json()
data=r[0]


for game in data:
    for team in data['events']:
        try:
            EpochTime = team['startTime']
            Epoch = datetime.datetime.fromtimestamp(EpochTime / 1e3)
            date = Epoch.strftime('%m-%d-%Y %H:%M:%S')
            team_1 = team['competitors'][0]['name']
            team_2 = team['competitors'][1]['name']
            try: odd_1_1 = team['displayGroups'][0]['markets'][1]['outcomes'][0]['price']['handicap'] 
            except KeyError: odd_1_1 = None
            try: odd_1_2 = team['displayGroups'][0]['markets'][0]['outcomes'][0]['price']['american'] 
            except KeyError: odd_1_2 = None
            try: odd_2_1 = team['displayGroups'][0]['markets'][1]['outcomes'][1]['price']['handicap'] 
            except KeyError: odd_2_1 = None
            try: odd_2_2 = team['displayGroups'][0]['markets'][0]['outcomes'][1]['price']['american'] 
            except KeyError: odd_2_2 = None
            try: ML_2 = team['displayGroups'][0]['markets'][1]['outcomes'][0]['price']['american']
            except KeyError: ML_2 = None
            try: ML_1 = team['displayGroups'][0]['markets'][1]['outcomes'][1]['price']['american']
            except KeyError: ML_1 = None
            try: o = team['displayGroups'][0]['markets'][2]['outcomes'][0]['price']['handicap']
            except KeyError: o = None
            try: o_1 = team['displayGroups'][0]['markets'][2]['outcomes'][0]['price']['american']
            except KeyError: o_1 = None
            try: u = team['displayGroups'][0]['markets'][2]['outcomes'][1]['price']['handicap']
            except KeyError: o = None
            try: u_1 = team['displayGroups'][0]['markets'][2]['outcomes'][1]['price']['american']
            except KeyError: o_1 = None
            # print(date)
            f.write("## **{0}** ({1},{2}) | {3} | o({4},{5}) at\r\n## **{6}** ({7},{8}) | {9} | u({10},{11})\r\n{12} MST\r\n\r\n".format(team_2,odd_1_1, odd_1_2, ML_2, o, o_1, team_1, odd_2_1, odd_2_2, ML_1, u, u_1, date))
            # print("{0} ({1},{2}) | {3} | u({4},{5})".format(team_1,odd_2_1, odd_2_2, ML_1, u, u_1))
        except KeyError: odd_1_1 = None
        except IndexError:
            pass
f.close()