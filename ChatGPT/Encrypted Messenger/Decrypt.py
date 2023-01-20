import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

# Decrypt the message with AES-RSA
def decrypt_message(encrypted_message: bytes, encrypted_aes_key: bytes, private_key: rsa.RSAPrivateKey) -> str:
    # Decrypt the AES key with the RSA private key
    aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    fernet = Fernet(aes_key)

    # Decrypt the message with the AES key
    decrypted_message = fernet.decrypt(encrypted_message).decode()

    return decrypted_message

# Test the decrypt_message function
encrypted_message = input("Enter the encrypted message: ")
encrypted_aes_key = input("Enter the encrypted key: ")

# Do not decode the entered strings
encrypted_message = encrypted_message.encode()
encrypted_aes_key = encrypted_aes_key.encode()

# Decrypt the message
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
decrypted_message = decrypt_message(encrypted_message, encrypted_aes_key, private_key)
print(f"Decrypted message: {decrypted_message}")
