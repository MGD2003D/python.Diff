def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    for i, char in enumerate(plaintext):
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword_repeated[i].upper()) - ord('A')
            offset = (ord(char) - start + shift) % 26
            ciphertext += chr(start + offset)
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword_repeated[i].upper()) - ord('A')
            offset = (ord(char) - start - shift) % 26
            plaintext += chr(start + offset)
        else:
            plaintext += char
    return plaintext