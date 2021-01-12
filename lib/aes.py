from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex
from lib.common import SUPPORTABLE_AES_KEY_LEN, AES_CFB_IV


class AesEncryption(object):
    def __init__(self, key, mode=AES.MODE_CFB):
        self.key = self.check_key(key)
        self.mode = mode
        self.iv = AES_CFB_IV

    def check_key(self, key):
        # checking lenght of key whether is supportable
        try:
            if isinstance(key, bytes):
                assert len(key) in SUPPORTABLE_AES_KEY_LEN
                return key
            elif isinstance(key, str):
                assert len(key.encode()) in SUPPORTABLE_AES_KEY_LEN
                return key.encode()
            else:
                raise Exception(
                    f"AES key must be str or bytes, cannot be {type(key)}"
                )
        except AssertionError:
            raise Exception(
                "current key length is not supportable"
            )

    def check_data(self, data):
        if isinstance(data, str):
            data = data.encode()
        elif isinstance(data, bytes):
            pass
        else:
            raise Exception(
                f"data which need to be encrypted must be str or bytes, "
                f"cannot be {type(data)}"
            )
        return data

    def encrypt(self, data):
        data = self.check_data(data)
        cryptor = AES.new(self.key, self.mode, self.iv)
        return b2a_hex(cryptor.encrypt(data)).decode()

    def decrypt(self, data):
        data = self.check_data(data)
        cryptor = AES.new(self.key, self.mode, self.iv)
        return cryptor.decrypt(a2b_hex(data)).decode()
