# ============================================================
# GIT BASH (terminal) - quick reference
# ============================================================
# Copy the line you need.

pwd                  # where am I?
ls                   # list files
ls -a                # also hidden files (.git, .gitignore)
cd folder            # go into a folder
cd ..                # go up one level
mkdir folder         # create a folder
mkdir -p a/b/c       # create nested folders
mv old new           # rename or move (not tracked by git: use git mv)
cp file copy         # copy a file
rm file              # delete a file (no trash, no undo)
rm -r folder         # delete a folder and its content
rmdir folder         # delete an EMPTY folder
cat file             # print a file
clear                # clean the screen

# Python on Windows with Git Bash:
py -m pip install pytest     # when `pip` is not found
python -m pytest -v          # when `pytest` is not found

# Tip: Tab completes names; Up arrow repeats the last command.
