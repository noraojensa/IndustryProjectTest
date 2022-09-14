from section_history.reqhistory import Entry, EntryList, get_history
from pathlib import Path
from git.repo import Repo
from datetime import datetime
import pytest

'''
def test_reqNotExist():
    reqID = "REQ222"
    directory = "/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/Dummy_project"
    assert reqHistory(reqID, directory) == '' #should maybe return an error message...
'''

'''def test_reqHistory():
    reqID = "REQ123"
    directory = "/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/Dummy_project"
    assert reqHistory(reqID, directory) == \'''    <requirement id = "REQ123"
                source="nora">
        
    Här är det nya fantastiska requirementet
    </requirement>
    <requirement id = "REQ123"
                source="jsiwj">
        
    Här är ett requirement REVISIONED VERSION!!!!
    </requirement>\n\'''
'''

'''
def test_newRepo(tmp_path: Path):

    #Print tmp_path!!!!
    repo_path = tmp_path / "repo"
    repo = Repo.init(repo_path) # type: ignore

    # This function just creates an empty file ...
    myfile = repo_path / "text.md"
    myfile.touch()
    myfile.write_text("<requirement id = \"REQ333\" source=\"jsiwj\"> This is a new requirement</requirement>")
    repo.index.add(["text.md"])
    repo.index.commit("initial commit") 
    repo.git.add(u=True)
    repo.index.commit("second commit")


    reqId = "REQ333"
    assert get_history(reqId, repo_path) == "<requirement id = \"REQ333\" source=\"jsiwj\"> This is a new requirement</requirement>"

'''

#Create a fixture to set up git repo!!
'''
@pytest.fixture
def set_up_repo(tmp_path: Path):
    repo_path = tmp_path / "repo"
    repo = Repo.init(repo_path) # type: ignore

    # This function just creates an empty file ...
    myfile = repo_path / "text.md"
    myfile.touch()
    reqID = "REQ333"
    myfile.write_text(f"<requirement id = {reqID} source=\"jsiwj\"> This is a new requirement</requirement>")
    repo.index.add(["text.md"])
    repo.index.commit("initial commit") 
    repo.git.add(u=True)
    repo.index.commit("second commit")
    return [reqID, repo_path]
'''


def test_stuff(tmp_path: Path):
    # set up git repo
    repo_path = tmp_path / "repo"
    repo = Repo.init(repo_path) # type: ignore

    # This function just creates an empty file ...
    myfile = repo_path / "text.md"
    myfile.touch()
    reqID = "REQ333"
    myfile.write_text(f"<requirement id = {reqID} source=\"jsiwj\"> This is a new requirement</requirement>")

    repo.index.add(["text.md"])
    repo.index.commit("initial commit") 
    repo.git.add(u=True)
    repo.index.commit("second commit")

    branch_name = "master"

    entries = get_history(reqID, repo_path, branch_name)
    print(entries)
    assert entries[0].text == f"<requirement id = {reqID} source=\"jsiwj\"> This is a new requirement</requirement>"


'''
def test_entry_convert_to_string():
    entry = Entry(text="<requirement...", author="Povel Ramel", date = datetime.now())

    assert str(entry) == "however you want to to have it look in the console"

def test_entry_list_to_str():
    entry_list = EntryList([Entry("..."), Entry("...")])

    assert str(entry_list) == "However you want it to look"

def test_invoke_from_console():
    # ensure that it can be run from the command line
    # in order to get code coverage of that functionality
'''

