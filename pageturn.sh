#!/bin/bash

if [ "$1" == "-b" ]; then
	cat page_back > /dev/input/event1
	exit 1
fi
if [ "$1" == "-f" ]; then
	cat page_forward > /dev/input/event1
	exit 1
fi

echo "Usage: ./pageturn.sh [-b | -f]"
exit 1
