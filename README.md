## Spoofing pageturns ##

Very simple Kindle pageturn application. Only tested on PW3 so far.

Requires jailbroken Kindle with remote shell access.

Copy contents of /pageturn to Kindle.

./pageturn.sh -b turns to previous page.

./pageturn.sh -f turns to next page.

page_back and page_forward are binary touchscreen event dumps from a Kindle Paperwhite 3. pageturn.sh simply sends them to /dev/input/event1.

## Debugging with input_read.py ##

input_read.py is code found at http://stackoverflow.com/a/16682549. Kindle touchscreen data passes "value" as a signed short, and the Kindle processor has 8-bit long ints (and thus, a 16-bit event struct). The Python script has been changed to reflect that.

To read input events, scp input_read.py to Kindle (requires Python installed on Kindle).

Run "python input_read.py" on Kindle to read out touchscreen event data from /dev/input/event1.

To test input_read without a Kindle, simply run it with page_back or page_forward as its first argument.
