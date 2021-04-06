#! /usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import isfile
import subprocess
import socket

def input_yn(_txt):
    _input = input(_txt).lower()
    if _input in ["y", "yes"]:
        return True
    return False

def local_ip():
    """
    socketを使ってローカルIPを取得
    Returns
    ----------
    get_ip : str
        取得したIPアドレス
    """
    get_ip = [
        (s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
        ][0][1]
    return get_ip

def getenv(_path):
    """
    update env param
    """
    if not isfile(_path):
        print(f"[info] not exist env file. {_path}")
        return {}

    # ファイル行読みしながらテキスト分析
    with open(_path, 'r', encoding="utf8") as f:
        ret = {}
        while True:
            line = f.readline()
            if line:
                spl = line.replace('\n', '').split("=", 2)
                ret[spl[0]] = spl[1]
            else:
                break
        return ret

def cmd_lines(_cmd, _cwd="", _encode='cp932', _wait_enter=False, _split=True):
    """
    execute command and stream text
    Parameters
    -----
    _cmd : list or str
        commands list
    _cwd : str
        current work dir.
    _encode : str
        default value cp932 (set utf-8 fix errors)
    """
    if isinstance(_cmd, list):
        for ref in _cmd:
            print(f"\n[info] command executed. [{ref}]")
            if _wait_enter:
                input("enter to execute cmd. ([ctrl + c] to cancel script)")
            cmd = ref
            if _split:
                cmd = ref.split()
            if _cwd == "":
                proc = subprocess.Popen(cmd
                                        , stdout=subprocess.PIPE
                                        , stderr=subprocess.STDOUT
                                        , shell=True)
            else:
                proc = subprocess.Popen(cmd
                                        , cwd=_cwd
                                        , stdout=subprocess.PIPE
                                        , stderr=subprocess.STDOUT
                                        , shell=True)
            while True:
                line = proc.stdout.readline()
                if line:
                    yield line.decode(_encode)
                if not line and proc.poll() is not None:
                    break
    else:
        print(f"\n[info] command executed. [{_cmd}]")
        if _wait_enter:
            input("enter to execute cmd. ([ctrl + c] to cancel script)")
        cmd = _cmd
        if _split:
            cmd = _cmd.split()
        if _cwd == "":
            proc = subprocess.Popen(cmd
                                    , stdout=subprocess.PIPE
                                    , stderr=subprocess.STDOUT)
        else:
            proc = subprocess.Popen(cmd
                                    , cwd=_cwd
                                    , stdout=subprocess.PIPE
                                    , stderr=subprocess.STDOUT)
        while True:
            line = proc.stdout.readline()
            if line:
                yield line.decode(_encode)
            if not line and proc.poll() is not None:
                break
