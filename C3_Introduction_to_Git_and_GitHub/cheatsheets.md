# Cheatsheets: git [working]

## base
- diff: show changes different between 2 files
- diff -u: used t compure 2 flie by lines
- patch: use for apllying differences
- log -p: show more infor about our changes
- show: show more IDs or Users
- --stat: show how much changes
- rm: remove
- mv: Move or rename a file
- checkout: undoing changes before commit
- commit --amend: easy change commit, overwrite the previous commit
- revert: undo
- clone: clone from git to local
- clone https://<nameuser><your_token>@github.com/username/repo.git : clone uses with your token

## Branching and Merging
- branch <name_branch>: create branch  
- checkout <name_branch>: switch to branch
- checkout -b <name_branch>: switch and create branch
- checkout -d <name_branch>: deleted branch
- merging <name_branch>: combines branch data and histories
- git merge --abort: If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.
- log --graph --online: show tree graph 
- log --graph --online --all: show the different commits and position in the tree 
- remote -v: 
- remote show origin: show information 
- git branch -r:
- git fetch:
- rebase <name_branch>:
- push--delete origin<name_branch>

## Forking
pull request: A commit or series of commits that you seng to the owner of the repo so that they incorporate it into their tree

## reset <commit>
- reset --hard|soft HEAD
- reset --hard HEAD^  :going back to the commit before HEAD
- reset --hard HEAD~1 :equivalent to "^"
- reset --hard HEAD~2 :going back two commits before HEAD

## Cherry-pick <commit>
- cherry-pick --continue: continue a pause cherry-pick operation
- cherry-pick --abort: abort an ongoing cherry-pick operation

## Undoing changes
- reset: reset staging area to match the last commit
- reset <commit>: remove a file form the last staging area
- reset --hard: discard all changes since the last commit  
- reset --hard <commit>: clear staging area, rewrite working tree from specified commit  

## Remote repo  
- remote -v: show list remote connection
- remote rm <remote>: remove remote
- remote show <remote>: show detail remote repo  
- remote rename <old_name> <new_name>: change name
- push --tags: push all tags
- push --force: push force
- push origin --delete <branch>: delete a remote
- pull --rebase: pull and rebase the current branch
- fetch: fetch update from all reomote repo
- fetch --all: fetch update from remote repo
- remote updates: update remote tracking branch

## Stashing: record the current state of the working directory and the index, but want to go back to a clean working directory
- stash: saving changes for later
- stash status: show list changes for later
- stash apply: apply
- stash drop: remove
- stash pop: rename and apply the last stash
- stash branch <name_branch>: create a new branch and apply a stash 
- stash save "<message>": 
- stash clear: remove all stash changes

## Tags:
- git tag # List tags
- git tag <tag-name> # Create a lightweight tag
- git tag -a <tag-name> -m "<message>" # Create an annotated tag
- git push origin <tag-name> # Push a tag to the remote repository
- git tag -d <tag-name> # Delete a local tag
- git push origin --delete <tag-name> # Delete a remote tag
- git tag --contains <commit> # Find tags containing a specific commit
- git describe # Describe the most recent tag and commit

## Traking Path Changes
- git ls-files # List all files tracked by Git
- git blame <file> # Show who changed what in a file
- git bisect # Find the commit that introduced a bug
- git reflog # Show a log of all local commits
- git cat-file -p <commit> # Display the content of a commit object
- git rev-parse <ref> # Get the SHA-1 hash of a reference
- git fsck # Verify the integrity of the repository
- git gc # Clean up unnecessary files and optimize the repository

## Advanced Commands
- git submodule add <repository> <path> # Add a Git submodule
- git submodule init # Initialize Git submodules
- git submodule update # Update Git submodules
- git submodule foreach <command> # Execute a command in all submodules
- git grep <pattern> # Search for a pattern in the repository
- git log -S"<pattern>" # Search for commits that added or removed a pattern
- git archive --format=zip --output=<output-file> <branch> # Create a zip archive of a branch
- git shortlog # Summarize commit logs by author
- git log --graph --decorate --oneline # Display commit history as a graph
- git rev-list --count <ref> # Count the number of commits in a branch
- git commit --amend # Modify the last commit
- git commit --amend -m "<new-message>" # Modify the last commit message
- git reflog expire --expire=now --all # Remove all reflog entries
- git rev-parse --show-toplevel # Show the root directory of the repository
- git config --global alias.<alias-name> '<git-command>' # Create a Git alias
- git help <command> # Show help for a Git command



## Reference
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges
