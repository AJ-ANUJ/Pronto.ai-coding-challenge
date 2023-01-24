from git import Repo
from datetime import datetime, timedelta



def git_repo_facts(repo_dir_path):    
    repo = Repo(repo_dir_path)
    print('active branch: ', repo.active_branch.name)

    hcommit = repo.head.commit
    index = repo.index
    file_modif = index.diff(hcommit)
    if(len(file_modif)>0):
        print('local changes: True')
    else:
        print('local changes: False')

    commit_date = hcommit.authored_datetime.replace(tzinfo=None)

    present_date = datetime.now()
    date_7 = present_date-timedelta(days=7)
    if(commit_date >= date_7):
        print('recent commit: True')
    else:
        print('recent commit: False')

    commit_author = hcommit.author.name
    if(commit_author=='Rufus'):
        print('blame Rufus: True')
    else:
        print('blame Rufus: False')
    

if __name__ == "__main__":
    repo_path = input('Enter the local git repository in the next line:\n')
    print('\n')
    git_repo_facts(repo_path)