from cryptopals import pals

with open("./cryptopals/extra/4.txt") as fp:
    given_file = fp.readlines()

for line in given_file:
    ct = bytes.fromhex(line)
    output = pals.xor_libs.brute_single_byte_xor(ct, 2)

    for each_member in output:
        try:
            pt = each_member[1].decode("utf-8")
            print(f"Encrypted text: {line}")
            print(f"Key: {each_member[0]}")
            print(f"Decrypted text: {pt}")
            print("-------\n")

        except UnicodeDecodeError:
            continue

"""
Encrypted text: 7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f

Key: 21
Decrypted text: nOWTHATTHEPARTYISJUMPING*
-------

Encrypted text: 7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f

Key: 53
Decrypted text: Now that the party is jumping
"""
