from cryptography.fernet import Fernet

# Generate a Key and Instantiate a Fernet Instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Text to be encrypted
text = b"Hello, World"
cipher_text = cipher_suite.encrypt(text)
print("Encrypted Text: ", cipher_text)

# Decrypt the Text
plaintext = cipher_suite.decrypt(cipher_text)
print("Decrypted Text: ", plaintext)