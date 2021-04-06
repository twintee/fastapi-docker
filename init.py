#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join, dirname, abspath, isdir
import sys
import shutil

import mod.helper as fn

dir_script = abspath(dirname(__file__))
os.chdir(dir_script)
file_env = join(dir_script, ".env")

def main():
    """
    initialize container
    """
    if not fn.input_yn("initialize container? (y/*) :"):
        print("[info] initialize canceled.")
        sys.exit()

    params = fn.getenv(file_env)

    # コンテナ削除
    cmd="docker-compose down"
    if fn.input_yn("initialize volumes? (y/*) :"):
        cmd="docker-compose down -v"
    for line in fn.cmd_lines(_cmd=cmd):
        sys.stdout.write(line)

    dir_logs = join(dir_script, "log")
    if isdir(dir_logs):
        if fn.input_yn("remove log dirs? (y/*) :"):
            shutil.rmtree(join(dir_script, "log"))

    # イメージリビルド
    cmd=f"docker-compose up -d"
    if fn.input_yn("rebuild image? (y/*) :"):
        for line in fn.cmd_lines(_cmd=f"docker rmi {params['IMAGE_NAME']}"):
            sys.stdout.write(line)
        for line in fn.cmd_lines(_cmd="docker-compose build", _encode='utf-8'):
            sys.stdout.write(line)

    # コンテナ作成
    if fn.input_yn("make container? (y/*) :"):
        for line in fn.cmd_lines(_cmd="docker-compose up -d", _encode='utf-8'):
            sys.stdout.write(line)
    else:
        print("[info] container make canceled.")
        sys.exit()

    print(f"""
[info] started. access to follow url.
http://{fn.local_ip()}
or
http://{params['VIRTUAL_HOST']}
""")


if __name__ == "__main__":

    print("[info] initialize start.")
    main()
    print("[info] initialize end.")
