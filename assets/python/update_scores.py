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
def getgame(index):
    return(listofgames[index])

for line in fileinput.input(my_file, inplace=1): 

    if re.search('^.*?\([^\d]*(\d+)[^\d]*\).*$', line):
        
        updatedGame = getgame(index)
        line = f"## **{updatedGame}** \r\n"
        index += 1
    sys.stdout.write(line)

        


