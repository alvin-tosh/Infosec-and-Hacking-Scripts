import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

# Generate a new RSA key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Extract the public key from the RSA key
public_key = private_key.public_key()

# Encrypt the message with AES-RSA
def encrypt_message(message: str, public_key: rsa.RSAPublicKey) -> tuple:
    # Generate a new AES key
    aes_key = Fernet.generate_key()
    fernet = Fernet(aes_key)

    # Encrypt the message with the AES key
    encrypted_message = fernet.encrypt(message.encode())

    # Encrypt the AES key with the RSA public key
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Return the encrypted message and encrypted AES key as a tuple
    return encrypted_message, encrypted_aes_key

# Test the encrypt_message function
message = input("Enter a message to encrypt: ")
encrypted_message, encrypted_aes_key = encrypt_message(message, public_key)
print(f"Encrypted message: {encrypted_message}")
print(f"Encrypted key: {encrypted_aes_key}")
