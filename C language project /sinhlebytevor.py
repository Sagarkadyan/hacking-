def single_byte_xor(input_bytes, key):
    return bytes([b ^ key for b in input_bytes])

def score_english(text):
    # Simple English character frequency
    freq = "ETAOIN SHRDLU"
    return sum([2 if chr(byte).upper() in freq else 0.5 if chr(byte).isalpha() else 0 for byte in text])

def break_single_byte_xor(cipher_hex):
    cipher_bytes = bytes.fromhex(cipher_hex)
    best_score = 0
    best_text = ""
    best_key = 0

    for key in range(256):
        decoded = single_byte_xor(cipher_bytes, key)
        try:
            score = score_english(decoded)
            if score > best_score:
                best_score = score
                best_text = decoded.decode('ascii', errors='ignore')
                best_key = key
        except:
            continue

    return best_key, best_text

# Test it
cipher_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
key, plaintext = break_single_byte_xor(cipher_hex)

print(f"Key: {chr(key)} (ASCII {key})")
print(f"Decrypted text: {plaintext}")
