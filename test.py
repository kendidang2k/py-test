from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64encode
import hashlib

def generate_md5_hash(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    md5_hash_hex = md5_hash.hexdigest()
    return md5_hash_hex

def hash_and_encrypt_RSA(public_key_str, message):
    # Load the public key
    public_key = RSA.import_key(public_key_str)

    # Encrypt the message hash with RSA using PKCS#1 v1.5 padding
    cipher = PKCS1_v1_5.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())

    # Return the encrypted message
    return b64encode(encrypted_message)

# Example usage
public_key_str = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0+B5KsZ/Q4c252WDMHVf4TPtoWwfTiikKu7NGkGaleBWZbDTyql4Cxf6aTMrIyqfYShGCVFWhJgNSmAbqkzvRr9BJVbyTVXppbTbeCKplpFso6IoMBXMizq3P+5VyvS+YFhPrCzDv5iFvMgnmkjlRm3rUZ0Nd22UdIh1Rvb3A/AnnzHR1PEqyYaS4/kzHgwKO0H404QTTA8Js67pA/WC4Bv/6fnE/GXMwsoWzZXwPeofSBkXFNsj2nrXROUfDzUmUQaMZT4monOt1ihzyRiF7+yHk6jmtFNU8KgrX2rnkqtpSCl524zFR9fztZplq2VqvpuefQNuBy3y5Ss1EnY24wIDAQAB
-----END PUBLIC KEY-----
"""
message = "Hello, world!"

hashed_and_encrypted_message = hash_and_encrypt_RSA(public_key_str, generate_md5_hash("Manman567@"))
print(hashed_and_encrypted_message.decode())
