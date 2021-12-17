import random


def gcd(a, b):
    '''Takes in two numbers a and b, returns the greatest common divisor.'''
    
    if(b == 0):
        R = a
    else:
        R = gcd(b, (a%b))
        
    return R


def isPrimeNumber(n):
    '''Takes in a number n, returns if the number is a prime number or not.'''
    # The Rabin-Miller algorithm is used
    # https://gist.github.com/Ayrx/5884790
    
    if n == 2:
        return True

    if n % 2 == 0:
        return False
    
    if n == 3:
        return True


    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(40):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def modularMultiplicativeInverse(a, b):
    '''Takes in two numbers a and b, returns the multiplicative inverse inverse of a by modulo b.'''
    
    i=1
    r=[]
    r.append(a) # r[0] = a
    r.append(b) # r[1] = len(alphabet)
    u=[]
    u.append(1) # u[0] = 1
    u.append(0) # u[1] = 0
    q=[]
    
    while(r[i] != 0):
        r.append(r[i-1]%r[i]) # r[i] = r[i-1]%r[i]
        q.append(r[i-1] // r[i]) # q[i] = r[i-1] // r[i]
        
        u.append(u[i-1]-(q[i-1]*u[i])) # u[i] = u[i-1]-(q[i-1]*u[i])
        
        i+=1
        
    return (u[i-1] % b)
    

def findPrimeNumber(Nb):
    '''Takes in a number Nb, returns a list of all prime numbers less than or equal to Nb.'''

    tab = [True]*(Nb+1)
    tab[0] = False
    tab[1] = False
    
    for i in range(2, (Nb//2)+1):
        b=2*i
        while b <= Nb:
            tab[b]=False
            b+=i
  
    primeNumber = []
    for i in range(0, len(tab)):
        if(tab[i]==True):
            primeNumber.append(i)
        
    return primeNumber


def findPQ(N):
    '''Takes in a number N, returns p and q two prime numbers whose product is N (0, 0 if p and q do not exist).'''

    primeNumber = findPrimeNumber(N)
    for p in primeNumber:
        if(p > N/2):
            return 0, 0
        
        if((N%p)==0):
            q = int(N/p)
            if(isPrimeNumber(q)):
                return p, q
        
    return 0, 0