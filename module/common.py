import os
def read_file(filename):
    with open(filename,'r') as f:
        data = f.read().splitlines()
        return data

def rm_output_file(filename):
    os.system("rm -rf output/" + filename)
    os.system("mkdir " + filename)