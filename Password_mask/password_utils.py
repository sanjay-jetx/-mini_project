from cryptography.fernet import Fernet


class FakeStr(str):

    def __repr__(self):
        return "*****"

    def __str__(self):
        return "*****"


def load_key():
    return open("secret.key", "rb").read()


def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())


def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)


def get_decrypted_password():

    encrypted_password = b'gAAAAABn7Cn_Wdov0yebXk-WJo2ctcoHMTsdnVEdjhLnhHoBsvq_KWcksne0Z910Z'

    return decrypt_password(encrypted_password)