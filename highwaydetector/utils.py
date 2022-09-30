import json, pickle, os, re, subprocess, shlex
import numpy as np
from glob import glob

def exec_cmd(cmd):
    print(f"LOG: exec_cmd({cmd})")
    try:
        raw_output = subprocess.check_output(shlex.split(cmd), universal_newlines=True)
        output = raw_output.split("\n")
        return output
    except subprocess.CalledProcessError as e:
        if (e.returncode == 124): # Special case for bash timeout command.
            return ['timeout']
        else:
            print(f"LOG: exec_cmd({cmd}) failed with err: {e.returncode}", f"\n{e.output}")
            return None

def read_json(pth):
    assert os.path.exists(pth), f"Path Not found: {pth} relative to {os.getcwd()}"
    with open(pth, 'r') as f:
        return json.load(f)
    
def to_json(obj, pth):
    with open(pth, 'w') as f:
        json.dump(obj, f)

def read_pickle(pth):
    assert os.path.exists(pth), f"Path Not found: {pth} relative to {os.getcwd()}"
    with open(pth, 'rb') as f:
        return pickle.load(f)

def to_pickle(obj, pth):
    with open(pth, 'wb') as f:
        pickle.dump(obj, f)

def read_txt(pth):
    assert os.path.exists(pth), f"Path Not found: {pth} relative to {os.getcwd()}"
    with open(pth, 'r') as fp:
        return fp.readlines()

def to_txt(lines, pth):
    with open(pth, 'w') as fp:
        for l in lines:
            fp.write("%s\n" % l)

def append_to_txt(lines, pth):
    with open(pth, 'a') as fp:
        for l in lines:
            fp.write("%s\n" % l)