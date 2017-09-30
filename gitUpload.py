from git import Repo

repo_dir = 'Temp'
repo = Repo(repo_dir)
file_list = [
    'im1.jpg'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
