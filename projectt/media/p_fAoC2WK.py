from backports.pbkdf2 import pbkdf2_hmac
print(pbkdf2_hmac("sha512","clave","0t1u2v3w4x5y6z7",25000,32))
