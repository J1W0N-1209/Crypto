from Crypto.Util.number import *

result = []

flag = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
flag = bytes.fromhex(flag)
crypto_flag = ""

for i in range(256):
    result = [chr(i ^ j) for j in flag]
    crypto_flag = "".join(result)

    if crypto_flag.startswith("crypto"):
        print(crypto_flag)
