#!/usr/bin/env python3

#my own
def decode_cesar(text, shift):
    cesar = dict(list((j + ord('a'), (j + shift) % 26 + ord('a')) for j in range(0, ord('z') + 1 - ord('a'))))

    return ''.join([chr(cesar.get(ord(letter), ord(letter))) for letter in text])

#expected
import string

def decode_cesar_good(text, shift):
    intab = string.ascii_lowercase
    outtab = ''.join([chr((ord(a) + 2 - ord('a')) % 26 + ord('a')) for a in intab])
    transtab = str.maketrans(intab, outtab)

    return text.translate(transtab)

print(decode_cesar("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpqypcdmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gqqmjmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.", 2))
print(decode_cesar("map", 2))

