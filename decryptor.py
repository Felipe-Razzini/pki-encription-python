import rsa

def decrypt_message(private_key):
    encrypted_message = open("encrypted.message", "rb").read()
    clear_message = rsa.decrypt(encrypted_message, private_key)

    return clear_message.decode()
