import requests
import json
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64encode
import rsa

url = "https://ops-api.namabank.com.vn/auth/personal/v3/login"

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

public_key_str = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0+B5KsZ/Q4c252WDMHVf4TPtoWwfTiikKu7NGkGaleBWZbDTyql4Cxf6aTMrIyqfYShGCVFWhJgNSmAbqkzvRr9BJVbyTVXppbTbeCKplpFso6IoMBXMizq3P+5VyvS+YFhPrCzDv5iFvMgnmkjlRm3rUZ0Nd22UdIh1Rvb3A/AnnzHR1PEqyYaS4/kzHgwKO0H404QTTA8Js67pA/WC4Bv/6fnE/GXMwsoWzZXwPeofSBkXFNsj2nrXROUfDzUmUQaMZT4monOt1ihzyRiF7+yHk6jmtFNU8KgrX2rnkqtpSCl524zFR9fztZplq2VqvpuefQNuBy3y5Ss1EnY24wIDAQAB
-----END PUBLIC KEY-----
"""

public_key = rsa.PublicKey.load_pkcs1_openssl_pem(public_key_str.encode())

ciphertext = hash_and_encrypt_RSA(public_key_str,generate_md5_hash("Manman567@"))

print("Encrypted:", ciphertext)

# js_encryptor = JSEncrypt(public_key=public_key)

# private_key, public_key = generate_rsa_key_pair()
# Example usage
# encrypted_password = encrypt_rsa(generate_md5_hash("Manman567@"), public_key)
# encrypted_result = js_encryptor.encrypt(generate_md5_hash("Manman567@"))

# ciphertext = encrypt_string_with_public_key(public_key, generate_md5_hash('Manman567@'))
# print("test: " + encrypted_result)

payload = json.dumps({
  "username": "0901547784",
  "password": ciphertext.decode()
})
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Origin': 'https://ops.namabank.com.vn',
  'Pragma': 'no-cache',
  'Referer': 'https://ops.namabank.com.vn/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'app-version': '2.0.0.0:Web',
  'browserId': '2.2.6.0',
  'checking': 'd3ba2b260c68e5f1981f2618bda9a4e7',
  'device-id': '',
  'device-info': 'Windows%3A10%3AChrome%3A12%3AUnknown',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'session-token': 'WEB-USER(8e3e590201b5bdcef1e05c1260a12ss3cwa)WEB-USER'
}

response = requests.request("POST", url, headers=headers, data=payload)

print("api res "+ response.text)
