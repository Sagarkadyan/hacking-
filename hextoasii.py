def fixed_xor(hex1, hex2):
    # Decode hex strings to bytes
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)

    # XOR corresponding bytes
    xor_result = bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))

    # Convert the result back to hex
    return xor_result.hex()

hex_input1 = "1c0111001f010100061a024b53535009181c"
hex_input2 = "686974207468652062756c6c277320657965"

result = fixed_xor(hex_input1, hex_input2)
print(result)
