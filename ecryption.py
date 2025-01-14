import string
import random

def cipher_caesar(k, m):
    return ''.join(chr((ord(char) + k) % 65536) for char in m)


def decipher_caesar(k, c):
    return ''.join(chr((ord(char) - k) % 65536) for char in c)


def hack_ceaser(s):
    possible_res = []
    max_freq = 0

    for shift in range(26):
        new_s = cipher_caesar(-shift, s)
        freq = sum(1 for char in new_s if
                    char.isalpha() or char.isspace())
        if freq >= max_freq:
            max_freq = freq
            possible_res += [new_s]

    return possible_res


def cipher_vernam(text, key):
    key_repeated = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key_repeated))


if __name__ == "__main__":
    message = "Hello, World!"
    caesar_key = 7
    ceaser_res = cipher_caesar(caesar_key, message)
    print("Цезарь, cipher:", ceaser_res)
    print("Цезарь, decipher:", decipher_caesar(caesar_key, ceaser_res))
    print("Возможные результаты взлома:", hack_ceaser(ceaser_res))

    vernam_key = ''.join(random.choice(string.ascii_letters) for _ in range(len(message)))
    vernam = cipher_vernam(message, vernam_key)
    vernam_res = cipher_vernam(vernam, vernam_key)
    print("Вижинер, cipher:", vernam)
    print("Вижинер, decipher:", vernam_res)
