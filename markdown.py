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

def convert_strong(line):
    line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
    return line

def convert_em(line):
    line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
    line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
    return line

def convert_headers(line):
    '''
    Converts
        ### ... -> <h3>...</h3>
        ## ... -> <h2>...</h2>
        # ... -> <h1>...</h1>
    Strips leading and trailing whitespace from the header declaration
    '''
    line = re.sub(r'^\s*###\s*(.*)\s*$', r'<h3>\1</h3>', line)
    line = re.sub(r'^\s*##\s*(.*)\s*$', r'<h2>\1</h2>', line)
    line = re.sub(r'^\s*#\s*(.*)\s*$', r'<h1>\1</h1>', line)
    return line

def strip_blockquote(line):
    if line.startswith('>'):
        return re.sub(r'^\>\s?(.*)$', r'\1', line), True
    else:
        return line, False

prev_is_blockquote = False
for line in fileinput.input():
    line = line.rstrip() 
    line, is_blockquote = strip_blockquote(line)
    line = convert_headers(line)
    line = convert_strong(line)
    line = convert_em(line)
    if not line.startswith('<h'):
        line = '<p>' + line + '</p>'
    if not prev_is_blockquote and is_blockquote:
        line = '<blockquote>' + line
    if prev_is_blockquote and not is_blockquote:
        line = '</blockquote>' + line
    prev_is_blockquote = is_blockquote
    print(line)
if prev_is_blockquote:
    print('</blockquote>')