from section_history.reqhistory import reqHistory
from pathlib import Path
from git.repo import Repo

'''
def test_reqNotExist():
    reqID = "REQ222"
    directory = "/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/Dummy_project"
    repo = Repo(directory)
    assert reqHistory(reqID, directory, repo) == '' #should maybe return an error message...
'''

'''def test_reqHistory():
    reqID = "REQ123"
    directory = "/Users/audurtheodorsdottir/Desktop/chalmers/2022stp1/DAT306/Dummy_project"
    repo = Repo(directory)
    assert reqHistory(reqID, directory, repo) == \'''    <requirement id = "REQ123"
                source="nora">
        
    Här är det nya fantastiska requirementet
    </requirement>
    <requirement id = "REQ123"
                source="jsiwj">
        
    Här är ett requirement REVISIONED VERSION!!!!
    </requirement>\n\'''
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
    assert reqHistory(reqId, repo_path, repo) == "<requirement id = \"REQ333\" source=\"jsiwj\"> This is a new requirement</requirement>"


    #collect_stats(repo_path, tmp_path / "log.csv", 1, 2)
    #return tmp_path / "log.csv"


