#!/usr/bin/python

import os
import sys
import email
import shutil
import email.parser
import pathlib
import hashlib

mail_base = os.path.expanduser('~/.mail')

def main():
    mail = email.parser.BytesParser().parse(sys.stdin.buffer)
    mail_bytes = mail.as_bytes()

    message_id = mail.get("Message-ID")
    mailbox = mail.get("X-getmail-retrieved-from-mailbox")

    md5_hash = hashlib.md5()
    md5_hash.update(message_id.encode('utf-8'))
    md5_digest = md5_hash.hexdigest()

    mailbox_path = os.path.join(mail_base, mailbox, 'new')
    if not os.path.isdir(mailbox_path):
        cur = os.path.join(mail_base, mailbox, 'cur')
        tmp = os.path.join(mail_base, mailbox, 'tmp')

        os.makedirs(mailbox_path)
        os.makedirs(cur)
        os.makedirs(tmp)

    with open(os.path.join(mailbox_path, md5_digest + '.txt'), 'wb') as f:
        f.write(mail_bytes)
main()
