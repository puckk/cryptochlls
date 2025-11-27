import random
import os
import requests
import time
from datetime import datetime, timezone
from Crypto.Cipher import AES

FLAG = "0bffd3591cb7644e8f94c567f5504819757323400c57f51bafe4075ea0dcfd093f70c0a9cdf53cb9834d49".encode()


def blend_key(key_bytes):
    key_int = int(key_bytes.hex(), 16)
    current_ts = int(time.time())
    print(
        f"{datetime.fromtimestamp(current_ts, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')} - Starting shuffling process"
    )
    key_int *= random.randint(1, 9999999)
    key_int *= random.randint(1, 1234567)
    key_int *= random.randint(1, 99999)
    key_int += 998877665544332211 * 13 // 9833 + 123456789
    key_int *= current_ts
    return key_int


def main():
    key = os.getenv("SECRET_KEY").encode()
    iv = b"product_security"
    cipher = AES.new(key, AES.MODE_OFB, iv)
    encrypted_flag = cipher.decrypt(FLAG)
    print(key)

if __name__ == "__main__":
    main()

