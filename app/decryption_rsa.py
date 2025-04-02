import app.cmath_rsa as cmath_rsa
def Decrypt_CRT(encrypted_message, e, p, q):
        d=cmath_rsa.inverse_mod(e,(p-1)*(q-1))
        x1=cmath_rsa.Binar_power_mod(encrypted_message,int(d)%int((p-1)),p)
        x2=cmath_rsa.Binar_power_mod(encrypted_message,d%(q-1),q)
        dm=cmath_rsa.garner_2(x1,x2,p,q)[0]        
        return(dm) 
    
def new_RSA(security): #1024 ≤ security ≤ 4096
    p=cmath_rsa.random_prime(security//2,security//2+100)
    q=cmath_rsa.random_prime(security//2,security//2+100)
    while p==q:
        q=cmath_rsa.random_prime(security//2,security//2+100)
    n=p*q
    phi_n=(p-1)*(q-1)
    e=65537
    d=cmath_rsa.inverse_mod(e,phi_n)
    return [p,q,n,phi_n,e,d]
