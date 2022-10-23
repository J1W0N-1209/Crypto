# 16진수를 바이트로 디코딩 한 후에 bas64로 인코딩

import base64

a = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
change_byte = bytes.fromhex(a)
print(base64.b64encode(change_byte))