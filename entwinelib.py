'''
Common entwine functions
'''

import os
import re
import datetime
import subprocess
import yaml

REMETA = re.compile(r'(?:---\n(?P<meta>.*?)\n---)?(?P<body>.*)', re.DOTALL)

def getmtime(path):
    '''
    Get mtime
    '''

    # Making it an int really shouldn't have been necessary but I've seen
    # minute differences as a result of copy2 which I can't explain.

    return int(os.stat(path).st_mtime)


def parsedate(date):
    '''
    Parse date
    '''

    with open(os.devnull, 'w') as fhl:
        proc = subprocess.Popen(['date', '-d', str(date), '+%s'],
                                stdout=subprocess.PIPE, stderr=fhl)
        try:
            return datetime.datetime.fromtimestamp(float(proc.communicate()[0]))
        except ValueError:
            return date


def loadmd(path):
    '''
    Load Markdown file, returning match with metadata and body
    '''

    with open(path) as fhl:
        match = REMETA.match(fhl.read())
        meta = match.group('meta')

        if meta:
            meta = yaml.load(meta)

            if 'date' in meta:
                meta['date'] = parsedate(meta['date'])

        return meta, match.group('body')
