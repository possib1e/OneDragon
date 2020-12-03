import os,csv
def start_oneforall(filename):
    os.chdir('./OneForAll')
    os.system("rm -rf results/")
    cmd ="python3 oneforall.py  --targets "+filename + " run"
    print(cmd)
    os.system(cmd)
    os.chdir('../')

if __name__ == '__main__':
    pass