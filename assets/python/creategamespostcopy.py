#!python 
import os
import re
import sys
import requests
import datetime
import json
import nflgame
from pytz import timezone

f= open("_posts/2019-11-13-stevespicksweek111.md","w+")
r = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl", verify=False).json()
data=r[0]

games = nflgame.games(2019, week=11)

listofgames = []
for g in games:
    listofgames.append(g)
    print(g.schedule['time'])


# def gethometeam():

#     return(f'{listofgames.home} {listofgames.score_home}')

# def getawayteam():
# return(f'{listofgames.away} {listofgames.score_away}')

# for game in data:

# for team in data['events']:
# try:
# EpochTime = team['startTime']
# Epoch = datetime.datetime.fromtimestamp(EpochTime / 1e3)
# date = Epoch.strftime('%m-%d-%Y %H:%M:%S')
# date1 = date.replace(tzinfo=timezone('ET'))
# team_1 = team['competitors'][0]['name']
# team_2 = team['competitors'][1]['name']
# try: odd_1_1 = team['displayGroups'][0]['markets'][1]['outcomes'][0]['price']['handicap'] 
# except KeyError: odd_1_1 = None
# try: odd_1_2 = team['displayGroups'][0]['markets'][0]['outcomes'][0]['price']['american'] 
# except KeyError: odd_1_2 = None
# try: odd_2_1 = team['displayGroups'][0]['markets'][1]['outcomes'][1]['price']['handicap'] 
# except KeyError: odd_2_1 = None
# try: odd_2_2 = team['displayGroups'][0]['markets'][0]['outcomes'][1]['price']['american'] 
# except KeyError: odd_2_2 = None
# try: ML_2 = team['displayGroups'][0]['markets'][1]['outcomes'][0]['price']['american']
# except KeyError: ML_2 = None
# try: ML_1 = team['displayGroups'][0]['markets'][1]['outcomes'][1]['price']['american']
# except KeyError: ML_1 = None
# try: o = team['displayGroups'][0]['markets'][2]['outcomes'][0]['price']['handicap']
# except KeyError: o = None
# try: o_1 = team['displayGroups'][0]['markets'][2]['outcomes'][0]['price']['american']
# except KeyError: o_1 = None
# try: u = team['displayGroups'][0]['markets'][2]['outcomes'][1]['price']['handicap']
# except KeyError: o = None
# try: u_1 = team['displayGroups'][0]['markets'][2]['outcomes'][1]['price']['american']
# except KeyError: o_1 = None
# # print(date)
    
        
#         time = ga.schedule['time'].replace(tzinfo=timezone('ET'))
        
            
#     # away = getawayteam()
#     # home = gethometeam()
#     ## {away} vs {home}\r\n
#     # f.write(f'## **{team_2}** ({odd_1_1},{odd_1_2}) | {ML_2} | o({o},{o_1}) at\r\n## **{team_1}** ({odd_2_1},{odd_2_2}) | {ML_1} | u({u},{u_1})\r\n{date} MST\r\n\r\n')
#     # index += 1
#     # print("{0} ({1},{2}) | {3} | u({4},{5})".format(team_1,odd_2_1, odd_2_2, ML_1, u, u_1))
# except KeyError: odd_1_1 = None
# except IndexError:
#     pass
# f.close()