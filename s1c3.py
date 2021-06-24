from cryptopals import pals

ct = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ct = bytes.fromhex(ct)
output = pals.xor_libs.brute_single_byte_xor(ct)

for each_member in output:
    try:
        pt = each_member[1].decode("utf-8")
        print(f"Key: {each_member[0]}")
        print(f"Decrypted text: {pt}")
        print("-------\n")

    except UnicodeDecodeError:
        continue

"""
Key: 88
Decrypted text: Cooking MC's like a pound of bacon
-------
"""
