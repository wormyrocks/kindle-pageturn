## Spoofing pageturns ##

Very simple Kindle pageturn application. Only tested on PW3 so far.

Requires jailbroken Kindle with remote shell access.

Copy page_back, page_forward, and pageturn.sh to Kindle.


./pageturn.sh -b turns to previous page.

./pageturn.sh -f turns to next page.


## Debugging with input_read.py ##

input_read.py is a slightly modified version of code found at http://stackoverflow.com/a/16682549.

To read input events, scp input_read.py to Kindle (requires Python installed on Kindle).

Run "input_read.py /dev/input/event1" to read out touchscreen event data.

page_back and page_forward are binary touchscreen event dumps from a Kindle Paperwhite 3. To test input_read without a Kindle, simply run it with page_back or page_forward as its first argument.
