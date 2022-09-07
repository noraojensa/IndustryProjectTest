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

def reqHistory(REQID, repo_path, repo):

    #directory = os.chdir("/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/IndustryProjectTest") #Directory in which the script looks for REQID -> Make dynamic
    #directory = Path.cwd() THE ONE WE'LL USE IN THE END
    #directory = "C:\\Users\\no\\Documents\\Dummy_project"

    #repo = Repo(directory)
    repo.git.checkout("master")

    searchString = str(repo_path) + '/*.md' #This should only look at markdown files, in accordance with how reqs are stored at Ericsson

    #Change! - Don't want it hard coded
    history_prints_left = 1
    prev_req = ""
    curr_req = ""
    total_req = ""

    while history_prints_left > 0:
        for filename in glob.glob(searchString):
            found = False
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                for line in f:
                    if REQID in line:
                        found = True
                    if found:
                        curr_req += line
                    if "</requirement>" in line:
                        break
            
            #hotfix solve later - need to exit while loop if REQID does not exist!!
            if history_prints_left == 1 and curr_req == '':
                history_prints_left = 0
            
            if curr_req != prev_req:
                print(curr_req)
                total_req += curr_req
                prev_req = curr_req
                history_prints_left = history_prints_left - 1
            curr_req = ""
            repo.git.checkout("HEAD~")

    repo.git.checkout("master")
    return total_req

if __name__ == "__main__":
    reqid = sys.argv[1] #User input REQID to print history for
    directory = "/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/Dummy_project"
    repo = Repo(directory)
    reqHistory(reqid, directory, repo)