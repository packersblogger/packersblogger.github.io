import os
import nflgame

f= open("_posts/2019-11-6-stevespicksweek10.md","w+")
games = nflgame.games(2019, week=10)


for g in games:
    
    f.write(f"## **{g}-{g.schedule['time']}** \r\n\r\n**PutLineHere**\r\ncontent_here\r\n\r\n**My Pick: **\r\n\r\n" )
    
f.close()