#!/usr/bin/python3

"""
Markdown script using python
"""

import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
                file=sys.stderr)
        exit(1)

    with open(sys.argv[1]) as read:
        with open(sys.argv[2], 'w') as html:
            unordered_start, ordered_start, paragraph = False, False, False
            # bold syntax
            for line in read:
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('_', '<em>', 1)
                line = line.replace('_', '</em>', 1)

                #md5

                md5 = re.findall(r'\[\[.+?\]\]', line)
                md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
                if md5:
                    line = line.replace(md5[0], hashlib.md5(
                        md5_inside[0].encode()).hexdigest())

                # remove the letter C
                remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
                remove_c_more = re.findall(r'\(\((.+?)\)\)', line)

                if remove_letter_c:
                    filtered_content = ''.join(
                        c for c in remove_c_more[0] if c not in 'Cc'
                        )
                    #Ensure replace is only called if there is content to replace
                    if remove_letter_c[0]:
                        line = line.replace(remove_letter_c[0], filtered_content)

                    html.write(line)
