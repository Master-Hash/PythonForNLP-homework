import os
import shutil
from zipfile import ZipFile

stuid = os.environ["stuid"]
name = os.environ["name"]

_homework_id = input("Homework ID: ")
homework_id = f"{_homework_id:0>2}"

if os.path.exists(f"src/{homework_id}.py"):
    shutil.copyfile(f"src/{homework_id}.py", f"build/{stuid}_{name}_{homework_id}.py")

with ZipFile(f"build/{stuid}_{name}_{homework_id}.zip", "w") as homework_zip:
    homework_zip.write(
        f"build/{stuid}_{name}_{homework_id}.py",
        arcname=f"{stuid}_{name}_{homework_id}.py",
    )

# 如果老师允许全部打包，可以用
# https://docs.python.org/zh-cn/3/library/shutil.html#shutil.make_archive
