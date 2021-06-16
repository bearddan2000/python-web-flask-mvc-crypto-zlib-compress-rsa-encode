import zlib

class PasswordCompress:

    def compress(self, password):
        # password = bytes(password, encoding='utf-8')
        return zlib.compress(password)

    def decompress(self, password):
        # password = bytes(password, encoding='utf-8')
        return zlib.decompress(password)
