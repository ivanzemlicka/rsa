import app.cmath_rsa as cmath_rsa
def Encrypt(message, e, n):
    em=cmath_rsa.Binar_power_mod(message, e, n)
    return em
