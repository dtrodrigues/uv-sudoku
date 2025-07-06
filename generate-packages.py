import os
import shutil

from util import boxes, intToBox, BASE_NAME


shutil.rmtree('packages', ignore_errors=True)
os.makedirs('packages', exist_ok=True)
os.chdir("packages")

for row in range(9):
    for col in range(9):
        for digit in range(1, 10):
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
            with open("pyproject.toml", "w") as f:
                f.write(tomlval)

            os.makedirs(f"src/{BASE_NAME}_{row+1}{col+1}", exist_ok=True)
            with open(f"src/{BASE_NAME}_{row+1}{col+1}/__init__.py", "w") as f:
                pass


            os.system(f"uv build --wheel")
