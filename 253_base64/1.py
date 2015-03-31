#!/usr/bin/env python

import encodings
import base64

encs = encodings.aliases.aliases.values()

us = base64.decodestring('4uTX1eTV2NWxw9Wl0tTHxmHzyGTB9OfmQkNk89Hz+LTx4rjXoqMAAKO0paHh0qFB88a3xuKmEA==')

for x in encs:
    try:
        print(us.decode(x))
    except:
        print('not %s ' % x)

