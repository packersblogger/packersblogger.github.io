import os
import nflgame

f= open("_posts/2019-10-30-stevespicksweek8.md","w+")
games = nflgame.games(2019, week=8)

for g in games:
    
    f.write(f"## **{g}** \r\n\r\n" )

f.close()