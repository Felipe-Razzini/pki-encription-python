import rsa
from datetime import datetime
from key_generator import generate_keys
from encryptor import encrypt_message
from decryptor import decrypt_message
from signer import sign_message
from verifier import verify_message

# Load or generate keys
try:
    with open("public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    with open("private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
except FileNotFoundError:
    public_key, private_key = generate_keys()

# Encrypt a message
message = "Order Confirmation: Your order #93860394 has been shipped and is on its way to your address."
encrypt_message(message, public_key)

# Decrypt the message
clear_message = decrypt_message(private_key)
print(clear_message)

# Sign a message
now = datetime.now()
message = f"Your Docusign account has been created at {now}. Please use email@test.com to login."
sign_message(message, private_key)

# To test if verification is working, change the message
# message = f"Your Docusign account has been created at {now}. Please use test@test.com to login."

# Verify the signature
with open("signature", "rb") as f:
    signature = f.read()

try:
    print(verify_message(message, signature, public_key))
except rsa.pkcs1.VerificationError:
    print("Verification failed. The message has been altered.")
