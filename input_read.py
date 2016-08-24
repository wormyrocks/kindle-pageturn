#!/usr/bin/python

#code taken from http://stackoverflow.com/questions/5060710/format-of-dev-input-event

import struct
import time
import sys

if len(sys.argv) < 2:
    infile_path = "/dev/input/event1"
else:
    infile_path = sys.argv[1]

#int, int, unsigned short, unsigned short, unsigned int
FORMAT = 'iihhi'
EVENT_SIZE = struct.calcsize(FORMAT)

#open file in binary mode
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

while event:
    (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

    if type != 0 or code != 0 or value != 0:
        print("Event type %u, code %u, value %u at %d.%d" % \
            (type, code, value, tv_sec, tv_usec))
    else:
        # Events with code, type and value == 0 are "separator" events
        print("===========================================")

    event = in_file.read(EVENT_SIZE)

in_file.close()
