import os,time,csv
import pandas as pd

def redup_ffuf(project):
    l = list()
    with open("../output/" + project + "/ffuf_all.csv",'r') as read:
        reader = csv.reader(read)
        for i in reader:
            l.append(i)
    df = pd.DataFrame(l)
    df.drop_duplicates(subset=5,keep="first",inplace=True)
    df.drop(df.index[0:1],inplace=True)
    df[1].to_csv("../output/" + project + "/ffuf_redup.txt",header=None,index=None)

def sum_ffuf(project):
    cwd = os.getcwd()
    get_dir = os.listdir(cwd+'/output/'+project)
    for i in get_dir:
        sub_dir = os.path.join(cwd+'/output/'+project,i)
        with open(sub_dir,"r") as f_read:
            with open("../output/" + project + "/ffuf_all.csv","a+") as f_write:
                f_write.write(f_read.read())

def read_file(filepath):
    with open(filepath,'r') as f:
        data = f.read().splitlines()
        return data

def start_ffuf(filename):
    os.chdir('./ffuf')
    os.system("mkdir output")
    os.system("rm -rf output/" + filename)
    os.system("mkdir output/" + filename)
    urls = read_file('../output/'+filename+'/all_urls.txt')

    for url in urls:
        cmd = "ffuf -w /root/tools/OneDragon/ffuf/dict/test-100.txt -u " + url + "/FUZZ -ac -o output/"+ filename + "/"+str(int(time.time()))+".csv -of csv"
        print(cmd)
        os.system(cmd)

    sum_ffuf(filename)
    redup_ffuf(filename)
    os.chdir('../')
def main():
    pass

if __name__ == '__main__':
    pass

