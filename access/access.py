import json
import os
import sys

def readJson(filename):
    dumped = None
    with open(filename, 'r') as f:
        dumped = json.loads(f.read())
    return dumped