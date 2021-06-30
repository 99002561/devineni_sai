import git
from pathlib import Path

Dir = "C:\\Users\\lekka\\PycharmProjects\\gittask"
g = git.Git("C:\\Users\\lekka\\Desktop\\GIT\\Mini-Project")
log_info = g.log()

# Replacing Notes with given output
lst = log_info.split("\n")
formatted = ""
for val in lst:
    if val.startswith('Notes:'):
        index = lst.index('Notes:')
        del lst[index - 2:index + 1]

# Output string Formatting
for val in lst:
    formatted += val
    formatted += '\n'

if Path(Dir).is_dir():
    print()
else:
    Path(Dir).mkdir(parents=True, exist_ok=False)
file = open('Commit_details.txt', 'w')
file.write(formatted)
file.close()

print("Commit history file is generated")
