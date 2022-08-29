## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Will create a clone/copy your repository onto the system you are using and connects them
  - `git clone`
- add
  - Adds tracking to a file in the git program
  - `git add filename`
- rm
  - Removes tracking to a file in the git program
  - `git rm filename`
- commit
  - Commits any changes made to tracked items in the respository
  - A brief description of what the commit is for will need to be written
  - `git commit`
- push
  - Pushes the commited changes out to your repository where everything is synced up
  - `git push`
- fetch
  - Grabs files from a remote repository and stores them on the local system
  - `git fetch`
- merge
  - Takes the changes made in one branch of a repository and merges them into another to combine the work history
  - `git merge nameofbranch`
- pull
  - Combines both fetch and merge commans
  - First it will fetch the files from the repository then automatically merge them into the branch
  - `git pull`
- branch
  - Creates a new branch of a repository that can be used as a secondary workspace that doesn't affect the main branch
  - `git branch nameofbranch`
- checkout
  - Used to switch from the current branch into another branch of the repository
  - `git checkout nameofbranch`
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
- .gitignore file
- ~~.git/hooks~~

## GitHub

- Pull requests
- SSH authentication to repositories
- ~~Actions~~
