def fixed_xor(buf1: bytes, buf2: bytes) -> bytes:
    """XOR two equal buffers

    Args:
        buf1 (bytes): First buffer to XOR
        buf2 (bytes): Second buffer to XOR

    Returns:
        bytes: XOR of the two buffers
    """

    from pwn import xor

    assert len(buf1) == len(buf2), "Buffers must be of equal length"

    return xor(buf1, buf2)


def analyze_frequency(buf: bytes) -> float:
    """Analyze frequency of letters in the given string

    Args:
        buf (bytes): The string for analysis

    Returns:
        float: Total score after the analysis
    """

    import json

    with open("./cryptopals/extra/letter_frequency.json") as f:
        frequency_dict = json.load(f)

    score = 0.0

    for letter in buf.lower():
        if letter >= 97 and letter <= 122:
            score += float(frequency_dict[chr(letter)])

    return score


def single_byte_xor(ct: bytes, key: int) -> bytes:
    """XOR a text with a single byte

    Args:
        ct (bytes): Ciphertext/plaintext
        key (int): The key to XOR with

    Returns:
        bytes: The result of the XOR
    """

    pt = b""

    for i in range(len(ct)):
        h = hex(ct[i] ^ key)[2:]
        h = "0" + h if len(h) == 1 else h
        pt += bytes.fromhex(h)

    return pt


def brute_single_byte_xor(ct: bytes, N: int = 5) -> [(int, bytes)]:
    """Brute force the string for single byte key and decrypt the string

    Args:
        ct (bytes): The string for brute forcing
        N (int)[ = 5]: Number of results to return, default 5
        
    Returns:
        [(int, bytes)]: The list of tuples of key and decrypted string
    """

    plaintexts = {}

    for key in range(256):
        xor_result = single_byte_xor(ct, key)
        plaintexts[xor_result] = key

    scores = {}

    for txt in plaintexts.keys():
        scores[txt] = analyze_frequency(txt)

    pt = []

    for txt in sorted(scores, key=lambda k: scores[k], reverse=True)[:N]:
        pt.append((plaintexts[txt], txt))

    return pt


def repeating_key_xor(pt: bytes, key: bytes) -> bytes:
    """Perform repeating key XOR

    Args:
        pt (bytes): The string to perform XOR on
        key (bytes): The key to XOR with

    Returns:
        bytes: String after performing repeating key XOR
    """

    key = (key * len(pt))[:len(pt)]
    
    return fixed_xor(pt, key)
