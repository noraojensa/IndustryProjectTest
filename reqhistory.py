import sys
import subprocess
import os

#TO-DO
# - Make while loop, which switches to earlier commit in the end, if none left loop ends
# - This prints out the REQ even if it hasn't changed -> save previous string and compare with new commit 
# - Code now breaks if input is a special character


REQID = sys.argv[1] #User input REQID to print history for
#os.chdir("C:/Users/no/Desktop/IndustryProjectTest") #Directory in which the script looks for REQID -> Make dynamic

found = False

file_with_req = subprocess.check_output(['grep', '-r', '-l', REQID], shell=True) #searches in current directory for the reqid
file_with_req = file_with_req.decode("utf-8")

file_with_req = file_with_req[:-1] #Removes trailing newline

with open(file_with_req,"r") as f:
    for line in f:
        if REQID in line:
            found = True
        if found:
            print(line)
        if "</requirement>" in line:
            break


#git stash
#git checkout HEAD~