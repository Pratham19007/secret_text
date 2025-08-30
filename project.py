# Caesar Cipher Project

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # sirf alphabets shift honge
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # spaces, numbers, symbols waise hi rahenge
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # decrypt karne ke liye opposite shift


# Main program
if __name__ == "__main__":
    print("=== Caesar Cipher Encryption & Decryption ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)