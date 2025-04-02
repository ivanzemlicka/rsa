class CMath:
    def inverse_mod(a,n):
        pass
        
    def Binar_power_mod(a,b,n):    
        result=1
        b_bin=[]
        while(b!=0):
            b_bin+=[b%2]
            b=b//2
        for i in reversed(b_bin):
            result=(result**2)%n
            if i==1: result=(result*a)%n
        return result

    def garner_2(r,m): #vstup delek 2
        r0=int(r[0])
        r1=int(r[1])
        m0=int(m[0])
        m1=int(m[1])
        mi=inverse_mod(m0,m1)
        x=(r0+m0*mi*(r1-r0))
        return [[x],[m0*m1]]
        
    def Val2(x):
        val=0
        while((x%2)==0):
            x=x//2
            val+=1
        return [val,x]
        
    def is_strong_probably_prime_to_base_a(n, val2, m, a):
        Z_n=Zmod(n)
        x=(a**m)%n #potreba zrychlit pomoci binarniho mocneni
        if x==Z_n(1) or x==Z_n(-1):
                return True
            
        for j in range(val2):
            x=Z_n(x*x)
            if x==Z_n(-1):
                return True
        return False
        
    def Rabin_Miller_test(n, precision): #4^-precision, is prime? 
        if n==2: return True
        if n==1: return False
        Z_n=Zmod(n)
        val=Val2(n-1)
        val2=val[0]
        d=val[1]
        for i in range (precision):
            a=Z_n.random_element()
            if (a!=Z_n(0) and (not is_strong_probably_prime_to_base_a(n, val2, d, a))):
                return False
        return True
        
    def random_prime(security,precision):
        x=secrets.randbits(security)
        x=x-(x%2)+1
        while(not Rabin_Miller_test(x,precision)):
            x+=2
        return x
    
class RSA_encryption:
    def __init__(self, prime_p, prime_q, n, phi_n, encryption_key_e, decryption_key_d):
        self.n=n
        self.e=enryption_key_e
        
    def Encrypt(self, message):
        em=Binar_power_mod(message,self.e,self.n)
        return em


class RSA_decryption:
    def __init__(self, prime_p, prime_q, n, phi_n, encryption_key_e, decryption_key_d):
        self.n=n
        self.e=encryption_key_e
        self.p=prime_p
        self.q=prime_q
        self.phi_n=phi_n
        self.d=decryption_key_d

    def Decrypt_CRT(self, encrypted_message):
        m=encrypted_message
        x1=CMath.Binar_power_mod(m,self.d%(self.p-1),self.p)
        x2=CMath.Binar_power_mod(m,self.d%(self.q-1),self.q)
        dm=CMath.garner_2([self.xy1,self.x2],[self.p,self.q])[0]        
        return(dm) 
    
    
    @classmethod
    def new_RSA(security): #1024 ≤ security ≤ 4096
        p=CMath.random_prime(security//2,security//2+100)
        q=CMath.random_prime(security//2,security//2+100)
        while p==q:
            q=CMath.random_prime(security//2,security//2+100)
        n=p*q
        phi_n=(p-1)*(q-1)
        e=65537
        d=inverse_mod(e,phi_n)
        return RSA_encryption(p,q,n,phi_n,e,d)
