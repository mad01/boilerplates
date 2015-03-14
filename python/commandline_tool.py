#!/usr/bin/env python
import argparse
import os
import subprocess


def cat(filename):
    command = "cat %s" % filename
    p = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, err = p.communicate()
    if len(out) > 0:
        print out

    if len(err) > 0:
        print err

if __name__ == "__main__":
    description = """
    write some description here
    """
    parser = argparse.ArgumentParser(description)
    parser.add_argument('-f', '--file', help='input file', required=True)
    parser.add_argument('-t', '--true', help='store true', action='store_true')
    parser.add_argument('-b', '--bar', help='input value bar', default='foo')
    parser.add_argument('-i', '--int', help='input int', type=int)
    parser.add_argument('-s', '--str', help='input str', type=str)
    args = parser.parse_args()

    file_path = os.path.abspath(os.path.abspath(args.file))
    file_name = os.path.basename(file_path)
    cat(file_path)
