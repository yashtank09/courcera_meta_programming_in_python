import importlib

# this is python_modules_filechanges python file that will show the directory contents
import python_modules_filechanges as pfc


# function to reflect changes of lib
def change():
    try:
        # again calling the imported module python_modules_filechanges
        importlib.reload(pfc)
        # print_changes() function will print the content of directory
        pfc.print_changes()
    except:
        pass

for i in range(5):
    # calling change function for showing updated directory, and it's content.
    change()
    # after hitting to enter it will reflect changes of updated directory contents
    input("Hit enter to reload...")

"""
# sys.path.insert() inserts or generate reference of given path
sys.path.insert(1, r'C:\Yash Stuff\Learning Stuff\Projects\courcera_meta_programming_in_python\Week 04\workplace')

# importing module which have only one print statement
import modtrials

# reload() function which reloads the import as much you call it.
reload(modtrials)
reload(modtrials)
"""
