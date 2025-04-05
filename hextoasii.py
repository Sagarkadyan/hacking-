import re

def hex_dump_to_ascii(filepath):
    hex_data = ""
    
    with open(filepath, "r", errors="ignore") as file:
        for line in file:
            match = re.match(r'^[0-9a-fA-F]{8}\s+((?:[0-9a-fA-F]{2}\s+)+)', line)
            if match:
                hex_part = match.group(1)
                hex_data += hex_part.strip().replace(" ", "")
    
    try:
        ascii_text = bytes.fromhex(hex_data).decode('utf-8', errors='ignore')
        print("\n[+] Decoded Output:\n", ascii_text)
        
        # Look for flag pattern
        flag = re.search(r'flag\{.*?\}', ascii_text, re.IGNORECASE)
        if flag:
            print("\n✅ Found Flag:", flag.group())
        else:
            print("\n⚠️ No flag found.")
    except Exception as e:
        print("❌ Error decoding hex:", e)

if __name__ == "__main__":
    filepath = "/home/sagar/Downloads/handout/glade.bat"  # Or use glade.bat
    hex_dump_to_ascii(filepath)
