import app.cmath_rsa as cmath_rsa

def new_RSA(security): #1024 ≤ security ≤ 4096
        p=cmath_rsa.random_prime(security//2,100)
        q= cmath_rsa.random_prime(security//2,security//8+10)
        while p==q:
            q=cmath_rsa.random_prime(security//2,security//8+10)
        n=p*q
        phi_n=(p-1)*(q-1)
        e=65537
        d=cmath_rsa.inverse_mod(e,phi_n)
        return [p,q,n,phi_n,e,d]
