#!python
import os
import nflgame

import re
import fileinput
import sys

games = nflgame.games(2019, week=9)

listofgames = []
for g in games:
    listofgames.append(g)
    
    
my_file = '_posts/2019-10-30-steviespicksweek9.md'

index = 0 
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
        
        line = f"## **{updatedGame}-{time}** \r\n"
        index += 1
    sys.stdout.write(line)

        


