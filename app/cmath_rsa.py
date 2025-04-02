import secrets
import random
def euclid(a,b):
    a1,a2=a,b
    u1,u2=1,0
    v1,v2=0,1
    while(a2!=0):
        r,q=divmod(a1,a2)
        a1,a2=a2,q
        u1,u2=u2,u1-r*u2
        v1,v2=v2,v1-r*v2
    return [a1,u1,v1]
    
def inverse_mod(a,n):
    eu=euclid(a,n)
    if eu[0]==1:
        return (eu[1])%n
    else:
        return "no inverse"
    
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

def garner_2(x1, x2 ,m1, m2): #vstup delek 2
    mi=inverse_mod(m1,m2)
    x=(x1+m1*mi*(x2-x1))
    return [x,m1*m2]
    
def Val2(x):
    val=0
    while((x%2)==0):
        x=x//2
        val+=1
    return [val,x]
  
def is_strong_probably_prime_to_base_a(n, val2, m, a):
    x=Binar_power_mod(a,m,n) 
    if x==1 or x==n-1:
            return True
        
    for j in range(val2):
        x=(x*x)%n
        if x==n-1:
            return True
    return False
    
def Rabin_Miller_test(n, precision): #4^-precision, is prime? 
    if n==2: return True
    if n==1: return False
    val=Val2(n-1)
    val2=val[0]
    d=val[1]
    for i in range (precision):
        a= random.randint(1, n)
        if (not is_strong_probably_prime_to_base_a(n, val2, d, a)):
            return False
    return True
    
def random_prime(security,precision):
    x=secrets.randbits(security)
    x=x-(x%2)+1
    while(not Rabin_Miller_test(x,precision)):
        x+=2
    return x
