#!/usr/bin/python

import os
import re
import sys
import email
import shutil
import email.parser
import pathlib
import hashlib

def prepend_email_patch_number(filepath):
    with open(filepath, 'r', errors="replace") as f:
        data = f.read()

    mail = email.parser.Parser().parsestr(data)
    subject = mail.get("Subject")
    patch = re.findall(r"\[(.*?)\]", subject)
    index = patch[0].split(" ")[-1].split("/")[0].lstrip()
    if int(index) == 0:
        os.remove(filepath)
        return

    index_str = "{0}-".format(index.zfill(4))
    new_filename = index_str + os.path.basename(filepath)
    new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
    os.rename(filepath, new_filepath)

def main():
    directory = os.path.join(sys.argv[1], "cur")
    files = [f for f in os.listdir(directory)]
    for f in files:
        prepend_email_patch_number(os.path.join(directory, f))
    
main()
