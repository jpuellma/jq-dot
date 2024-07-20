#!/usr/bin/env python

import fileinput

for fileinput_line in fileinput.input():
    if "Exit" == fileinput_line.rstrip():
        break
    print(f"Processing Message from fileinput.input() {fileinput_line}")

