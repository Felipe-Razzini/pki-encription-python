import rsa

def verify_message(message, signature, public_key):
    return rsa.verify(message.encode(), signature, public_key)
