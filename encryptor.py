import rsa

def encrypt_message(message, public_key):
    encrypted_message = rsa.encrypt(message.encode(), public_key)

    with open("encrypted.message", "wb") as f:
        f.write(encrypted_message)
