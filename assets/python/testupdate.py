import os
import sys
import fileinput
import nflgame
import re

# f= open("_posts/2019-10-30-stevespicksweek8.md","w+")
def replaceAll(file,replaceExp):
    for line in fileinput.input(file, inplace=1):
        searchExp = line.startswith("## **")
        if searchExp in line:
            line = line.replace(str(searchExp),replaceExp)
        sys.stdout.write(line)
games = nflgame.games(2019, week=8)
for g in games:
    replaceAll(r"_posts/2019-10-23-steviespicksweek8.md", f'## **{g}** \r\n\r\n')
    # f.write(f"## **{g}** \r\n\r\n" )

# f.close()