def hex2base64(buf: bytes) -> bytes:
    """Perform base64 encoding

    Args:
        buf (bytes): Buffer to perform base64 encoding on

    Returns:
        bytes: Base64 encoding
    """

    from base64 import b64encode

    return b64encode(buf)