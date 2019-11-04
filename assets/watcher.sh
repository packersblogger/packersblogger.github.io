#!/bin/bash

while true
do
    # source /home/r3weber/Desktop/packersblogger.github.io/assets/ENV/bin/activate
    # python /home/r3weber/Desktop/packersblogger.github.io/assets/python/update_scores.py
    # calculate time range
    currentSec=$(date "+%s")
    currentTime=$(date "+%Y%m%d %T")

    previousSec=$(echo "$currentSec-3600" | bc)
    previousTime=$(date "+%Y%m%d %T" --date="@$previousSec")

    echo "--- $previousTime - $currentTime ---"
    currentPath=$(pwd)
    workingPath="$1"

    cd "$workingPath"
    echo "now here: $workingPath"

    find . -type f -newermt "$previousTime" ! -newermt "$currentTime" -print | xargs git add .

    git commit -v -m "changes from $previousTime - $currentTime"
    git push origin master
    
    cd "$currentPath"
    echo "now here: $currentPath"

    # wait for 1 hour
    sleep 30m
done