# Mapboard

# Uses an address via CLI arg or Clipboard contents (default) to Google search
# a street address.

# WHY DO THIS? It makes our life easier (maybe).

# Manually Getting a Map
#   - Highlight the address
#   - Copy the address
#   - Open the web browser
#   - Go to http://maps.google.com/
#   - Click the address text, paste the address.
#   - Press enter.
# Using mapIt.py?
#   - Highlight the address/copy the address
#   - Run mapIt.py

# IMPORTS #####################################################################

import sys
import webbrowser as wb
import pyperclip as pc

# DEF #########################################################################

# MAIN ########################################################################

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pc.paste()

print(address)
site = wb.open('https://www.google.com/maps/place/' + address)
