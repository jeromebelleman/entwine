import os

def getmtime(path):
    '''
    Get mtime
    '''

    # Making it an int really shouldn't have been necessary but I've seen
    # minute differences as a result of copy2 which I can't explain.

    return int(os.stat(path).st_mtime)
