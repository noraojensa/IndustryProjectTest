import sys
import subprocess
import os
from pathlib import Path
from git.repo import Repo
import glob
import datetime
from dateutil.relativedelta import relativedelta
import pytz

#TO-DO
# - Make while loop, which switches to earlier commit in the end, if none left loop ends
# - This prints out the REQ even if it hasn't changed -> save previous string and compare with new commit 
# - Code now breaks if input is a special character

def get_history(REQID, repo_path):

    #directory = os.chdir("/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/IndustryProjectTest") #Directory in which the script looks for REQID -> Make dynamic
    #directory = Path.cwd() THE ONE WE'LL USE IN THE END
    #directory = "C:\\Users\\no\\Documents\\Dummy_project"

    repo = Repo(repo_path)
    repo.git.checkout("main")

    searchString = str(repo_path) + '/*.js' #This should only look at markdown files, in accordance with how reqs are stored at Ericsson

    prev_req = ""
    curr_req = ""
    total_req = ""
    today = datetime.datetime.now()
    one_year_ago = today - relativedelta(years=1)
    utc=pytz.UTC
    
    

    while one_year_ago.replace(tzinfo=utc) < repo.head.commit.committed_datetime.replace(tzinfo=utc):
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
            
            if curr_req != prev_req:
                print(curr_req)
                total_req += curr_req
                prev_req = curr_req

            curr_req = ""
            repo.git.checkout("HEAD~")
  
        if glob.glob(searchString) == []:
            break


    repo.git.checkout("main")
    return total_req

if __name__ == "__main__":
    reqid = sys.argv[1] #User input REQID to print history for
    directory = "C:\\Users\\no\\Documents\\Dummy_project"
    #directory = "/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/Dummy_project"
    get_history(reqid, directory)