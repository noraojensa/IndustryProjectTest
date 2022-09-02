#!/bin/bash

#TO-DO
# - Make while loop, which switches to earlier commit in the end, if none left loop ends
# - This prints out the REQ even if it hasn't changed -> save previous string and compare with new commit 

cd /Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/IndustryProjectTest
found=False

file=$(grep -r -l "<requirement")

while IFS=  read -r line; do 
    if [[ "$line" == *"<requirement"* ]]; then #kollar om REQID hittats på en rad
        found=True
    fi
    if $found; then #om REQID hittats printa varje rad 
        echo $line
    fi
    if [[ "$line" == *"</requirement>"* ]]; then #tills </Requirement> hittas, vilket bryter hela loopen
        break
    fi    
done < $file

#git stash
#git checkout HEAD~
