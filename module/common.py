import shutil
from pathlib import Path


OUTPUT_ROOT = Path("output")


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def rm_output_file(filename):
    output_dir = OUTPUT_ROOT / Path(filename).name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
