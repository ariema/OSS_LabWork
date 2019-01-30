"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def createHeaders(line):
    line = re.sub(r'^\s*###\s*(.*)\s*$', r'<h3>\1</h3>', line)
    line = re.sub(r'^\s*##\s*(.*)\s*$', r'<h2>\1</h2>', line)
    line = re.sub(r'^\s*#\s*(.*)\s*$', r'<h1>\1</h1>', line)
    return line

def stripBlockquote(line):
    if line.startswith('>'):
        return re.sub(r'^\>\s?(.*)$', r'\1', line), True
    else:
        return line, False   

prevBQ = False
for line in fileinput.input():
    line = line.rstrip() 
    line, isBQ = stripBlockquote(line)
    line = createHeaders(line)
    line = convertStrong(line)
    line = convertEm(line)
    if not line.startswith('<h'):
        line = '<p>' + line + '</p>'
    if not prevBQ and isBQ:
        line = '<blockquote>' + line
    if prevBQ and not isBQ:
        line = '</blockquote>' + line
    prevBQ = isBQ
    print(line)
if prevBQ:
    print('</blockquote>')