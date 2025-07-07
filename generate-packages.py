import os
import shutil
import subprocess

from util import boxes, intToBox, BASE_NAME

shutil.rmtree('packages', ignore_errors=True)
os.makedirs('packages', exist_ok=True)

shutil.rmtree('wheels', ignore_errors=True)
os.makedirs('wheels', exist_ok=True)

def generate_package(row, col, digit):
    deplist = set()
    for x in range(0,9):
        if x != row:
            deplist.add(f"\"{BASE_NAME}_{x+1}{col+1}!={digit}\"")
    for x in range(0,9):
        if x != col:
            deplist.add(f"\"{BASE_NAME}_{row+1}{x+1}!={digit}\"")
    myPos = row * 9 + col
    box = intToBox[myPos]
    for x in boxes[box]:
        if x != myPos:
            deplist.add(f"\"{BASE_NAME}_{x//9+1}{x%9+1}!={digit}\"")

    tomlval = f"""
[project]
name = "{BASE_NAME}_{row+1}{col+1}"
version = "{digit}"
requires-python = ">=3.13"
dependencies = [{", ".join(deplist)}]

[build-system]
requires = ["uv_build>=0.7.19,<0.8"]
build-backend = "uv_build"
"""
    currentPackageDir = f"packages/{BASE_NAME}_{row+1}{col+1}_{digit}"
    os.makedirs(currentPackageDir, exist_ok=True)
    with open(f"{currentPackageDir}/pyproject.toml", "w") as f:
        f.write(tomlval)

    os.makedirs(f"{currentPackageDir}/src/{BASE_NAME}_{row+1}{col+1}", exist_ok=True)
    with open(f"{currentPackageDir}/src/{BASE_NAME}_{row+1}{col+1}/__init__.py", "w") as f:
        pass

    subprocess.run(["uv", "build", "--wheel", "-o", "../../wheels/"], cwd=currentPackageDir, capture_output=True, text=True)



from concurrent.futures import ThreadPoolExecutor
params = [(row, col, digit) for row in range(9) for col in range(9) for digit in range(1, 10)]
with ThreadPoolExecutor() as executor:
    executor.map(lambda args: generate_package(*args), params)
