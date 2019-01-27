#!/usr/bin/env python3
import subprocess,os,argparse
#take any args and pass them to ssh
from subprocess import PIPE
from os.path import expanduser,dirname
SSH_KEYS="~/.ssh/authorized_keys"
DEFAULT_PUBLIC_KEY="~/.ssh/id_rsa.pub"
DEFAULT_PRIVATE_KEY="~/.ssh/id_rsa"
SSH_COMMAND="ssh"

def _prep_auth_append(public_key_file,wipe_existing_keys=True,file_check=True):
    with open(expanduser(public_key_file),'r')as inp:
        file_data=inp.read()
        #check if the file supplied is a private key file
        if file_check:
            if _test_private(file_data):
                try:
                    public_key=_extract_public
                raise ValueError("Supplied a private key file, requires public key")
        return "mkdir -p {0}{1};{2}".format(dirname(SSH_KEYS),";rm -f %s"%SSH_KEYS,"echo \"%s\" > %s"%(file_data,SSH_KEYS))
#if prompted for password and enter_password then
def _extract_public(private_key_file,enter_password=True):
    _args=["ssh-keygen","-y","-f",expanduser(private_key_file)]
    if not os.path.exists(private_key_file):raise FileNotFoundError(private_key_file)
    with subprocess.Popen(_args,stdin=PIPE,stdout=PIPE,stderr=PIPE)as p:
        a=p.stdin.read()
        print(a)
        #if y'all got a different language y'all fukd
        if "enter passphrase:" in tdecode(a):
            if
        else:return tdecode(a)

def upload_that_shit(public_key_file,ssh_password=None,disable_ssh_password_authentication=True):
    pass
def _is_private(file):
    with open(file,'r')as inp:
        if inp.read()
def tdecode(d):
    try:d.decode()
    except:return d
def _test_private(fdata):return "-----BEGIN RSA PRIVATE KEY-----" in tdecode(fdata)
def test():
    #print(_prep_auth_append("~/.ssh/id_rsa.pub"))

def main():
    pass

if __name__=="__main__":
    main()
