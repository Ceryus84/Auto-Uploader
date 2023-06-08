"""
Aidan Butcher
A simple program that will run in the background and upload a given dictionary
of files in a directory to a github repository. It should make a new repository
for each file which is tied to the key name and the file name is the value.
Requires that the PyGitHub library is installed. Requires that an access token
be provided,
Todo: Properly create a function or class to handle all of this.
      Set up the time checking system. Work on creating background services.
      Future: Create a text GUI to make interaction easier. If time permits,
              create an actual GUI with tkinter or other library.
Bugs: None.
"""

import shutil, os, time
from github import Github

ACCESS_TOKEN = ""
UPLOAD_DIR = "files_to_upload"
UPLOADED_DIR = "files_uploaded"
USER = ""
repo_dict = {}
count = 0

# Sets up the Github object and gets the authenticated user.
g = Github(ACCESS_TOKEN)
user = g.get_user()

# Creates a new repository, writes a new file, reads the new content to a
# new file in the repository. 
user.create_repo("test_repo", "Test repository creation.")
repo = g.get_repo(USER + "/test_repo")
with open("test.txt", 'w') as t:
    t.write("File will be uploaded to github repo.")
with open("test.txt", 'r') as t2:
    content = t2.read()
repo.create_file("test.txt", "test commit", content)


# Handles file movement on OS, currently only works on local PC.
"""while True:
    if len(os.listdir('files_to_upload')) == 0 or count == 1:
        print("Directory is empty.")
        break
    for filename in os.listdir('files_to_upload'):
        if filename.endswith('py'):
            dot_ind = list(filename).index('.')
            repo_name = str(filename[:dot_ind])
            repo_dict = {repo_name: filename}
            #shutil.move('files_to_upload\\' + filename, 'files_uploaded')
    count += 1
    time.sleep(6)

print(repo_dict)"""
