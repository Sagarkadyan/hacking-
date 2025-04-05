# debughex2bin.py
# Simulate what debug.exe does from glade.hex

def parse_debug_hex():
    lines = []
    with open("/home/sagar/Downloads/handout/glade.bat", "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("echo"):
                lines.append(line.lower())

    memory = {}
    current_addr = 0
    for line in lines:
        if line.startswith("e "):  # edit command
            parts = line.split()
            current_addr = int(parts[1], 16)
        elif all(c in "0123456789abcdef " for c in line.replace(" ", "")):
            for byte_str in line.split():
                memory[current_addr] = int(byte_str, 16)
                current_addr += 1
        elif line.startswith("r cx"):
            pass  # skip
        elif line.startswith("w") or line.startswith("q"):
            pass  # skip

    return memory

def write_binary(memory, output="glade"):
    with open(output, "wb") as f:
        for addr in sorted(memory):
            f.write(bytes([memory[addr]]))
    print(f"✅ Rebuilt binary saved as: {output}")

memory = parse_debug_hex()
write_binary(memory)



