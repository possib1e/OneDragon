
def read_file(filename):
    with open(filename,'r') as f:
        data = f.read().splitlines()
        return data