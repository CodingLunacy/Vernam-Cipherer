#Python 3.8.5
import string
import random

def pan_key(plain_text: str="", size: int=0) -> str:
    """Generates and returns a pan key based on given length.

    Parameters
    ----------
    plain_text: str
        The plain_text which needs a pan_key generated based
        on length of the plain_text

    size: int
        The length of a given pan_key wanting to be returned

    Returns
    -------
    str:
        A generated pan_key based on the length of plain_text
        or a given size
    """
    return "".join(
        [random.choice(string.printable) for i in range(
            size or len(plain_text)
            )
         ]
        )

def cipher(pan_key: str, plain_text: str) -> str:
    """Takes in a pan key and plain text, then ciphers the text.

    Parameters
    ----------
    pan_key: str
        The pan_key of the given plain text, has to be exactly the
        same length to function correctly, using XOR to cipher the
        text

    plain_text: str
        The plain_text to be ciphered

    Returns
    -------
    str:
        The new ciphered plain_text

    """
    cipher_text = ""
    for i in range(len(plain_text)):
        # Performs XOR operation with each character
        # in the plain text and pan key
        cipher_text += chr(ord(pan_key[i]) ^ ord(plain_text[i]))
    return cipher_text

if __name__ == "__main__":
    while True:
        plain_text = str(input("\n\nEnter plain text!\n:"))
        key = pan_key(plain_text)
        ciphered = cipher(key, plain_text)
        print("\nPan key:\n{key}".format(key=key))
        print("\nCiphered:\n{ciphered}".format(ciphered=ciphered))
