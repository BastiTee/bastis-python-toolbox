r"""This module contains command line call tools."""

from platform import system
import subprocess
import os

def runcommand (command, suppress_stdout=False, suppress_stderr=False,
                useshell=True, workdir=None):
    """Run a command on the command line"""
    
    log_stdout = []
    handle = subprocess.Popen(command, shell=useshell, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, cwd=workdir)
        
    while handle.poll() is None:
        line = handle.stdout.readline().strip()
        if not line == None:
            log_stdout.append(line)
            if suppress_stdout == False:
                print line
    
    log_stderr = log_stdout
    return handle.returncode, log_stdout, log_stderr

def checkforcommand(name):
    """Tests whether an executable with the given name exists on the path"""
    
    try:
        devnull = open(os.devnull)
        subprocess.Popen([name], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True

def get_platform():
    """Returns the system's platform string"""
    
    platform = str(system()).lower()
    return platform    
