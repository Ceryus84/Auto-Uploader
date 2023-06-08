"""
Aidan Butcher
A simple program that will run in the background and upload a given dictionary
of files in a directory to a github repository. It should make a new repository
for each file which is tied to the key name and the file name is the value.
Requires that the PyGitHub library is installed.
Todo: Set up dictionary that holds repository names and the corresponding
      filename. Upload said files to the corresponding repository using
      PyGithub module.
Bugs: Having an authentication error with github, need to make an access token.
      Once that is finished it should work, if not try following the docs
      explicity.
"""

import shutil, os, time
from github import Github

g = Github()
for repo in g.get_user().get_repos():
    print(repo.name)

"""
while True:
    if len(os.listdir('files_to_upload')) == 0:
        print("Directory is empty.")
        break
    for filename in os.listdir('files_to_upload'):
        if filename.endswith('py'):
            shutil.move('files_to_upload\\' + filename, 'files_uploaded')
    time.sleep(6)
"""
