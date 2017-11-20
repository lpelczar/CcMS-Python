import hashlib


class PasswordService:

    @staticmethod
    def encrypt_password(password):
        secure_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return secure_hash

    @staticmethod
    def verify_password(password, secure_hash):
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return True if password_hash != secure_hash else False
