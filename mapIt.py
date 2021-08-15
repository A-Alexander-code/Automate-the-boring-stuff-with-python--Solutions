# python3
# mapIt.py - lauches a map in the browser using an anddres from the
# command line or clipboard

import pyperclip, webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # TODO: Get addres from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)