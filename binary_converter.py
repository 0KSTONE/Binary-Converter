#!/usr/bin/env python3
"""
Simple Binary ↔ Text/Number Converter

- Converts Unicode text ↔ 8‑bit binary strings (UTF-8 encoding).
- Converts integer numbers ↔ binary strings.
- Presents a menu so the human operator selects which direction to use.
"""

import datetime

def text_to_binary(text: str) -> str:
    """
    Convert text to a space‑separated string of 8‑bit binary values (UTF-8 encoding).
    """
    return ' '.join(f"{byte:08b}" for byte in text.encode('utf-8'))

def binary_to_text(bin_str: str) -> str:
    """
    Convert a space‑separated string of 8‑bit binary values to text (UTF-8 decoding).
    Raises ValueError if any chunk isn’t valid 8‑bit binary.
    """
    chunks = bin_str.split()
    try:
        byte_array = bytearray(int(chunk, 2) for chunk in chunks)
        return byte_array.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Invalid UTF-8 binary input: {e}")

def int_to_binary(number: int) -> str:
    """
    Convert an integer to its binary representation (no leading '0b').
    """
    return bin(number)[2:]

def binary_to_int(bin_str: str) -> int:
    """
    Convert a binary string (e.g. '1101') to an integer.
    Raises ValueError if bin_str contains non‑'0'/'1' characters.
    """
    if any(c not in '01' for c in bin_str):
        raise ValueError(f"Invalid binary number: '{bin_str}'")
    return int(bin_str, 2)

def save_to_file(content: str, conversion_type: str):
    """
    Save the given content to a new file with a timestamp and conversion type in the filename.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversion_{conversion_type}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Result saved to {filename}")

def main():
    menu = """
Select conversion mode:
1) Text → Binary (UTF-8, 8‑bit per byte)
2) Binary (8‑bit, UTF-8) → Text
3) Integer → Binary
4) Binary → Integer
0) Exit
"""
    while True:
        print(menu)
        choice = input("Enter choice [0‑4]: ").strip()
        if choice == '0':
            print("Exiting converter.")
            break

        try:
            if choice == '1':
                text = input("Enter Unicode text: ")
                binary = text_to_binary(text)
                print(f"Binary (UTF-8, 8‑bit per byte): {binary}")
                save = input("Save result to file? (y/n): ").strip().lower()
                if save == 'y':
                    save_to_file(binary, "text_to_binary")

            elif choice == '2':
                bin_str = input("Enter space‑separated 8‑bit binary (UTF-8, e.g. '01100001 01100010'): ").strip()
                text = binary_to_text(bin_str)
                print(f"Decoded UTF-8 text: {text}")
                save = input("Save result to file? (y/n): ").strip().lower()
                if save == 'y':
                    save_to_file(text, "binary_to_text")

            elif choice == '3':
                num_str = input("Enter integer number: ").strip()
                number = int(num_str)
                binary = int_to_binary(number)
                print(f"Binary representation: {binary}")
                save = input("Save result to file? (y/n): ").strip().lower()
                if save == 'y':
                    save_to_file(binary, "int_to_binary")

            elif choice == '4':
                bin_str = input("Enter binary number (e.g. '1101'): ").strip()
                number = binary_to_int(bin_str)
                print(f"Integer value: {number}")
                save = input("Save result to file? (y/n): ").strip().lower()
                if save == 'y':
                    save_to_file(str(number), "binary_to_int")

            else:
                print(f"Unrecognized option: '{choice}'. Please pick 0‑4.")

        except ValueError as ve:
            print(f"Error: {ve}")

        print()  # Blank line before showing the menu again

if __name__ == "__main__":
    main()
