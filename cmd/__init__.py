import os
import subprocess
from v2 import log


# 打开

# os.system("cd ~")
# os.system("open ～/Documents/dy_download")


def open_dir(dir_path):
    # 打开文件目录
    os.open(path=dir_path)


def run_cmd(cmd_str):
    result = subprocess.run(cmd_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    print("out:", result.stdout)
    print("err:", result.stderr)
    print("check_returncode:", result.returncode)  # 非0


# cmd = "open ～/Documents/dy_download"
# run_cmd(cmd)

def user_home():
    # 获取当前用户的主目录路径
    path = os.path.expanduser('~')
    print(path)
    return path


