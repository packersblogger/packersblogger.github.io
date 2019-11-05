import requests
import re
import datetime
import json


i=2
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
                listofodds.append("{0} ({1},{2}) | {3} | o({4},{5})".format(team_2,odd_1_1, odd_1_2, ML_2, o, o_1))
                # print("{0} ({1},{2}) | {3} | u({4},{5})".format(team_1,odd_2_1, odd_2_2, ML_1, u, u_1))
            except KeyError: odd_1_1 = None
            except IndexError:
                pass
    return(listofodds[i])
print(getodds(i))