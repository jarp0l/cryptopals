from cryptopals import pals

pt = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

pt = bytes.fromhex(pt)

print(pals.encoding_libs.hex2base64(pt).decode())
