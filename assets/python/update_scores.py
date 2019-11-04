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
    if g.winner == g.away:
        winningscore = g.score_away
        losingscore = g.score_home
        difference = winningscore - losingscore

        print (f'{g.away} by {difference}')
    else:
        winningscore = g.score_home
        losingscore = g.score_away
        difference = winningscore - losingscore

        print (f'{g.home} by {difference}')  
    # if g.winner:
    #     print(f'{g.winner}')
    #     continue
    # else:
    #     print('none')
    
    
# my_file = '_posts/2019-10-30-steviespicksweek9.md'

# index = 0 
# def getgame(index):
#     return(listofgames[index])
# def gettime(index):
#     gameTime = listofgames[index].time
#     if gameTime.is_pregame():  
#         return("{} ET".format(listofgames[index].schedule['time']))
#     else:
#         return(gameTime)
    
# for line in fileinput.input(my_file, inplace=1): 

#     if re.search('^.*?\([^\d]*(\d+)[^\d]*\).*$', line):
        
#         updatedGame = getgame(index)
#         time = gettime(index)
        
#         line = f"## **{updatedGame}-{time}** \r\n\r\n"
#         index += 1
#     sys.stdout.write(line)

        


