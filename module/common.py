import shutil
import os


OUTPUT_ROOT = "output"


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def rm_output_file(filename):
    output_dir = os.path.join(OUTPUT_ROOT, os.path.basename(filename))
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
