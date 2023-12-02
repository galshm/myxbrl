# myxbrl
This is my python code to analyze XBRL files from the TASE stock exchange

# First time installation

### From "start" Open "Anaconda prompt(miniconda3)"
- `conda update -n base -c defaults conda`
- `conda create -n myxbrl python=3.11`
- `conda activate myxbrl` ==> DONT FORGET TO ALWAYS ACTIVATE!! 

# git instructions
## Update branch from main
- When in \<branch\> perform the following operations:
- `git fetch`
- `git rebase origin/main`
## Deliver to main from sub branch
- `git checkout main`
- `git pull` # to update the state to the latest remote master state
- `git merge <sub branch name>` # to bring changes to local master from your develop branch
- `git push origin main` # push current HEAD to remote master branch

## gitignore
remove a file if already checked in:
- `git rm --cached FILENAME`
Check status of specific file:
- `git check-ignore -v FILENAME`