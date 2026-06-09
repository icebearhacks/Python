#!/usr/bin/env python3
import base64
import struct
import sys

try:
    from Cryptodome.Hash import MD4
except ImportError:
    from Crypto.Hash import MD4

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} {FILENAME}.b64")
    sys.exit(1)

blob = base64.b64decode(open(sys.argv[1], "rb").read())

version, reserved, length, cur_off, prev_off, query_off, unchanged_off = struct.unpack("<HHIHHHH", blob[:16])

i = cur_off
while i + 1 < len(blob):
    if blob[i:i+2] == b"\x00\x00":
        break
    i += 2

password_bytes = blob[cur_off:i]

h = MD4.new()
h.update(password_bytes)
ntlm = h.hexdigest()

print(f"NTLM: {ntlm}")
