from Crypto.Cipher import AES
import base64
import re
import sys

def decrypt_aes_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.rstrip(b'\0')

def process_password_file(filename):
    key_bytes = bytes.fromhex("7D5A39D625A10A476FAD6AB519C4E092")
    iv_bytes = bytes.fromhex("6D4A7FD2C4A791B48E4296A6B3CF765D")

    with open(filename, 'r') as file:
        for line in file:
            encoded_data = line.strip()
            try:
                ciphertext = base64.b64decode(encoded_data)
                plaintext = decrypt_aes_cbc(ciphertext, key_bytes, iv_bytes)

                match = re.search(r'"([^"]*)"', plaintext.decode(errors='ignore'))
                if match:
                    password = match.group(1)
                    print("Пароль:", password)
                else:
                    print("Правильный пароль не найден.")
            except Exception as e:
                print("Ошибка, неверный формат пароля:", e)

def main():
    if len(sys.argv) != 2:
        print("Использование: python 1c_pass_cracker.py <имя_файла>")
        sys.exit(1)

    filename = sys.argv[1]
    process_password_file(filename)

if __name__ == "__main__":
    main()
