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
  - Combines both fetch and merge commands
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
  - Stores all the neccesary information to run your git repository
  - Things like commit information, logs and references are stored in there
  - Branch and tracking information is also stored
- .gitignore file
  - Used to specify certain files that you want to have on your local system in the repository location but do not want git to track
- ~~.git/hooks~~

## GitHub

- Pull requests
  - A request sent to the the main git repository when work that has been done on a seperate branch has been completed
  - The request can be accepted or denied to be merged into the main branch of the repository
  - They also allow for discussions to be made about the work before it is merged
- SSH authentication to repositories
  - A secure and passwordless connection between GitHub and a remote system
  - Uses SSH keys to provide authentication
  - A private key is placed on the local system and a public key is placed onto GitHub
  - When the connection is attempted it will make sure that the keys are the correct ones for each other to authenticate
- ~~Actions~~
