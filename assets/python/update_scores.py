#!python 
import os
import nflgame
import re
import fileinput
import sys

games = nflgame.games(2019, week=8)

listofgames = []
for g in games:
    listofgames.append(g)
    
    
my_file = '_posts/2019-10-23-stevespicksweek8.md'

index = 0 
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
    
    if re.search('^.*?\([^\d]*(\d+)[^\d]*\).*$', line):
        
        updatedGame = getgame(index)
        time = gettime(index)
        winner = getwinner(index)
        line = f"## **{updatedGame}-{time}**\r\n**{winner}** \r\n"
        index += 1
    sys.stdout.write(line)

        


