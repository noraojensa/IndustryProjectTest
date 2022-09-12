import sys
import os
from pathlib import Path
from git.repo import Repo
import glob
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Entry:
    file: str
    commit: str
    author: str
    date: datetime
    text: str

class EntryList(list):
    def __str__(self) -> str:
        return '\n\n'.join(self)

    # Default str for list objects:
    #[the first entry, the next entry, ...]

    # Wanted str for this entry list object
    # to display it better in the console
    """the first entry

    the second entry

    ..."""


def add_entry_info(repo, filename, current_section):
    #history = ""
    #history += f"File: {filename} \nCommit: {repo.head.commit.hexsha} \nAuthor: {repo.head.commit.author} <{repo.head.commit.author.email}> \nDate: {repo.head.commit.committed_datetime} \n\n{current_section} \n -------------------------------------------------------------\n\n"
    #return history
    new_entry = Entry(
        filename, 
        repo.head.commit.hexsha, 
        f"{repo.head.commit.author} <{repo.head.commit.author.email}>", 
        f"{repo.head.commit.committed_datetime}", 
        current_section)
    return new_entry


def get_history(REQID, repo_path):

    #Initiates git repo
    repo = Repo(repo_path)
    repo.git.checkout("main")

    searchString = str(repo_path) + '/*.js' #This should only look at markdown files, in accordance with how reqs are stored at Ericsson
    #previous_section = Entry("","","",None,"")
    #current_section = Entry("","","",None,"")
    current_section = ""
    history = []
    num_of_changes = 0

    #For every file in directory of repo
    for filename in glob.glob(searchString):
        #Breaks when file no longer exists, i.e before file was created
        while filename in glob.glob(searchString):
            found = False
            #Looks for section specified (only looks for one instance per file maybe change?)
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                for line in f:
                    if REQID in line:
                        found = True
                    if found:
                        current_section += line
                    if "</requirement>" in line:
                        break           

            #If section has changed from last commit, add current section to output. Counts nr. of changes.
            if found == True and (history == [] or current_section != history[-1].text):
                history.append(add_entry_info(repo, filename, current_section))
                num_of_changes += 1
            #Jump one commit back
            current_section = ""
            repo.git.checkout("HEAD~")
        #Return to newest commit again
        repo.git.checkout("main")
    return f"\nNumber of changes for {REQID}: {num_of_changes}\n\n {history}"

if __name__ == "__main__":
    reqid = sys.argv[1] #User input REQID to print history for
    #directory = "C:\\Users\\no\\Documents\\Dummy_project"
    directory = "/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/Dummy_project"
    #directory = Path.cwd() THE ONE WE'LL USE IN THE END
    print(get_history(reqid, directory))