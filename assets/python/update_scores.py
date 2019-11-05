#!python 
import os
import nflgame
import re
import fileinput
import sys
import requests
import datetime
import json

games = nflgame.games(2019, week=10)

listofgames = []
for g in games:
    listofgames.append(g)
    
    
my_file = '_posts/2019-11-6-stevespicksweek10.md'

index = 0 
i = 0
def getodds(i):
    r = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl", verify=False).json()
    data=r[0]
    listofodds = []
    
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
                listofodds.append("**{0}** ({1},{2}) | {3} | o({4},{5}) at **{6}** ({7},{8}) | {9} | u({10},{11})-{12}".format(team_2,odd_1_1, odd_1_2, ML_2, o, o_1, team_1, odd_2_1, odd_2_2, ML_1, u, u_1, date))
                # print("{0} ({1},{2}) | {3} | u({4},{5})".format(team_1,odd_2_1, odd_2_2, ML_1, u, u_1))
            except KeyError: odd_1_1 = None
            except IndexError:
                pass
    return(listofodds[i])

def getwinner(index):
    if listofgames[index].game_over():

        if listofgames[index].winner == listofgames[index].away:
            winningscore = listofgames[index].score_away
            losingscore = listofgames[index].score_home
            difference = winningscore - losingscore

            return (f'{listofgames[index].away} by {difference}')
        else:
            winningscore = listofgames[index].score_home
            losingscore = listofgames[index].score_away
            difference = winningscore - losingscore

            return (f'{listofgames[index].home} by {difference}')
    else:
        return ('not final')
    

def getgame(index):
    return(listofgames[index])
def gettime(index):
    gameTime = listofgames[index].time
    if gameTime.is_pregame():  
        return("{} ET".format(listofgames[index].schedule['time']))
    else:
        return(gameTime)
    
for line in fileinput.input(my_file, inplace=1): 
    
    # if re.search('^.*?\([^\d]*(\d+)[^\d]*\).*$', line):
    if re.search('[0-9]{2}-[0-9]{2}-[0-9]{4}', line):  
        # updatedGame = getgame(index)
        # time = gettime(index)
        # winner = getwinner(index)
        odds = getodds(i)
        # line = f"## **{updatedGame}-{time}**\r\n**{winner}** \r\n**{odds}**\r\n"
        line = f"## {odds}\r\n"
        index += 1
        i += 1
    sys.stdout.write(line)

        


