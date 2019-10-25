#!python
import os
import nflgame

games = nflgame.games(2019, week=8)
listofgames = []
for g in games:
    listofgames.append(g)
    

my_file = '_posts/2019-10-23-steviespicksweek8.md'

with open(my_file, 'r') as file:
    lines = file.readlines()

# length = len(lines)
# i =0
def getgame():
   
    for index, item in enumerate(listofgames):
        return item
        item = index + 1


starts = [lines.index(l) for l in lines if l.startswith('##')]
# game = [listofgames for ga in listofgames]
  
for s in starts:
    game = getgame()
    lines[(s + 1)]= f'**Actual: {game}**\r\n\r\n'
    #     break
# while i < length:
   
        
            
#         
            # i += 1
            
with open(my_file, 'w') as file:
    file.writelines(lines)
file.close()
        


