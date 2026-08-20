from passlib.context import CryptContext

cryptoContext = CryptContext(schemes=["argon2"], deprecated='auto')

def hash_password1(password):
    return cryptoContext.hash(password)

def verify_password(password, hashed_password):
    return cryptoContext.verify(password, hashed_password)

salt = "SuperSecretKey"

# def hash_password(password):
#     hash = "12hello34$#@%%@" + password + salt
#     return hash


# def verify_password(password, hash_password):
#     if password in hash_password:
#         return password


