from cryptopals import pals

ct1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
ct2 = bytes.fromhex("686974207468652062756c6c277320657965")

solution = "746865206b696420646f6e277420706c6179"

assert (
    pals.xor_libs.fixed_xor(ct1, ct2).hex() == solution
), "Error! Check the implementation once more."

print(pals.xor_libs.fixed_xor(ct1, ct2).hex())
