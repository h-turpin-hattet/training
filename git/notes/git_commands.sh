# ============================================================
# GIT - quick reference (commands used so far)
# ============================================================
# Not meant to be run as a script: copy the line you need.


# -- Check where you are ------------------------------------
git status                 # what changed, what is staged
git log --oneline          # history, one line per commit
git diff                   # changes not yet staged
git remote -v              # URL of the GitHub repo (origin)


# -- Daily cycle: add -> commit -> push ---------------------
git add notes/lists.py     # stage ONE file (explicit, no `git add .`)
git commit -m "docs: add lists notes"
git push                   # send to GitHub
git push -u origin main    # first push of a branch (-u = remember it)
git pull                   # get changes from GitHub


# -- Commit message: Conventional Commits (in English) ------
# type: short description
#   feat:     new feature
#   fix:      bug fix
#   docs:     notes, README
#   test:     tests
#   refactor: reorganize code or files, same behavior
#   chore:    small maintenance (.gitignore, config)


# -- Move / rename / delete (git keeps the history) ---------
git mv old.py new.py       # rename or move a tracked file
git rm file.py             # delete a tracked file
git rm --cached file.py    # stop tracking, keep the file on disk
git rm -r --cached __pycache__   # same for a folder


# -- .gitignore ---------------------------------------------
# Text file at the repo root, one pattern per line:
#   __pycache__/
#   .pytest_cache/
#   .venv/
# It does NOT untrack files already committed: use
# `git rm --cached` first, then commit.


# -- Repo on GitHub -----------------------------------------
git clone <url>                       # download a repo
git remote set-url origin <new-url>   # after renaming the repo
gh repo rename <new-name>             # rename from the terminal (gh CLI)


# -- Pitfalls -----------------------------------------------
# - Empty folders are not tracked: add a file inside.
# - A folder with its own .git inside a repo shows as a
#   submodule (arrow on GitHub): delete the inner .git folder.
# - Forgot a file in the last commit, not pushed yet:
#   git add <file> ; git commit --amend --no-edit
