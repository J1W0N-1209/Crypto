from Crypto.Util.number import *

result = []

flag = '54586b6458754f7b215c7c75424f21634f744275517d6d'
flag = bytes.fromhex(flag)
crypto_flag = ""

for i in range(256):
    result = [chr(i ^ j) for j in flag]
    crypto_flag = "".join(result)

    if crypto_flag.startswith("DH"):
        print(crypto_flag)
