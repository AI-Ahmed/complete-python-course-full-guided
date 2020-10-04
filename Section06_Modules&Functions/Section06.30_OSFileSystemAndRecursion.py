__author__ = "crypto"

import os

listing = os.walk('.')  # generate a file names in a directory tree by walking the tree either up-down

for root, directories, files in listing:
    print(root)
    for d in directories:
        print(d)
        for file in files:
            print(file)
# ------------------------------------------------------------------------------
print('=' * 40)


# let's create a function that list the directories

def list_dir(s):

    def dir_list(d):
        # global tab_stop    # unfortunate, this time scoping the variable will not help us to make it work, so we need to specify the scope of the variable in situation like that
        # 'nonlocal' won't check the global name space though so a 'nonlocal' variable must exist in the enclosing scope but not be global otherwise
        # if it was 'global' of course you would use the key 'global' to do that.
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory" + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + "does not exist")


list_dir('.')
