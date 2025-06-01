#!/usr/bin/env python3
"""
Simple Binary ↔ Text/Number Converter

- Converts ASCII text ↔ 8‑bit binary strings.
- Converts integer numbers ↔ binary strings.
- Presents a menu so the human operator selects which direction to use.
"""

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

def main():
    menu = """
Select conversion mode:
1) Text → Binary (8‑bit ASCII)
2) Binary (8‑bit ASCII) → Text
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
                text = input("Enter ASCII text: ")
                binary = text_to_binary(text)
                print(f"Binary (8‑bit per char): {binary}")

            elif choice == '2':
                bin_str = input("Enter space‑separated 8‑bit binary (e.g. '01100001 01100010'): ").strip()
                text = binary_to_text(bin_str)
                print(f"ASCII text: {text}")

            elif choice == '3':
                num_str = input("Enter integer number: ").strip()
                number = int(num_str)
                binary = int_to_binary(number)
                print(f"Binary representation: {binary}")

            elif choice == '4':
                bin_str = input("Enter binary number (e.g. '1101'): ").strip()
                number = binary_to_int(bin_str)
                print(f"Integer value: {number}")

            else:
                print(f"Unrecognized option: '{choice}'. Please pick 0‑4.")

        except ValueError as ve:
            print(f"Error: {ve}")

        print()  # Blank line before showing the menu again

if __name__ == "__main__":
    main()
