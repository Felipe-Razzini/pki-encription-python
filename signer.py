import rsa

def sign_message(message, private_key):
    signature = rsa.sign(message.encode(), private_key, "SHA-256")

    with open("signature", "wb") as f:
        f.write(signature)
