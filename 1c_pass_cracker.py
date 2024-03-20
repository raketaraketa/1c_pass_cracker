from Crypto.Cipher import AES
import base64
import re

def decrypt_aes_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.rstrip(b'\0')

def main():
    encoded_data = input("Введите закодированный пароль: ")
    key_bytes = bytes.fromhex("7D5A39D625A10A476FAD6AB519C4E092")
    iv_bytes = bytes.fromhex("6D4A7FD2C4A791B48E4296A6B3CF765D")

    ciphertext = base64.b64decode(encoded_data)

    # Расшифровка AES в режиме CBC
    plaintext = decrypt_aes_cbc(ciphertext, key_bytes, iv_bytes)

    # 
    match = re.search(r'"([^"]*)"', plaintext.decode(errors='ignore'))
    if match:
        password = match.group(1)
        print("Пароль:", password)
    else:
        print("Правильный пароль не найден.")

if __name__ == "__main__":
    main()
