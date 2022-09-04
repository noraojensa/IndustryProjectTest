import sys
import subprocess
import os
from pathlib import Path
from git.repo import Repo
import glob

#TO-DO
# - Make while loop, which switches to earlier commit in the end, if none left loop ends
# - This prints out the REQ even if it hasn't changed -> save previous string and compare with new commit 
# - Code now breaks if input is a special character

REQID = sys.argv[1] #User input REQID to print history for
#directory = os.chdir("/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/IndustryProjectTest") #Directory in which the script looks for REQID -> Make dynamic
#directory = Path.cwd() THE ONE WE'LL USE IN THE END
directory = "C:\\Users\\no\\Documents\\Dummy_project"
repo = Repo(directory)
repo.git.checkout("main")

searchString = str(directory) + '/*.js' #This should only look at markdown files, in accordance with how reqs are stored at Ericsson

history_prints_left = 2
prev_req = ""
curr_req = ""

while history_prints_left > 0:
    for filename in glob.glob(searchString):
    #find a way to see how many commits there have been in total!!!
        found = False
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
        #text = f.read()
            for line in f:
                if REQID in line:
                    found = True
                if found:
                    curr_req += line
                if "</requirement>" in line:
                    break
        
        if curr_req != prev_req:
            print(curr_req)
            prev_req = curr_req
            history_prints_left = history_prints_left - 1
        curr_req = ""
        repo.git.checkout("HEAD~")

repo.git.checkout("main")

#file_with_req = subprocess.check_output(['grep', '-r', '-l', REQID], shell=True) #searches in current directory for the reqid
#file_with_req = file_with_req.decode("utf-8")

#print(file_with_req)

#file_with_req = file_with_req[:-1] #Removes trailing newline

'''

for elem in range(5):
    found = False
    with open(text,"r") as f:
        for line in f:
            if REQID in line:
                found = True
            if found:
                print(line)
            if "</requirement>" in line:
                break

    repo.git.checkout("HEAD~")

repo.git.checkout("minorFixes")

'''


#git stash
#git checkout HEAD~