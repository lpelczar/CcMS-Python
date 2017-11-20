import hashlib


class PasswordService:

    @staticmethod
    def encrypt_password(password):
        secure_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return secure_hash
