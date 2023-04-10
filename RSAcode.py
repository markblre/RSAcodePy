import mathsTools

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def prepaCrypt(M):
    '''Takes in a string M, returns a string that is M coded.'''
    
    validChoice = False
    while not validChoice:
        choice = input("1) I enter p and q\n2) I enter N. p and q will be deducted\n--> ")
        if(int(choice)==1):
            validChoice = True
            p = int(input("p = "))
            while not mathsTools.isPrimeNumber(p):
                print("p must be a prime number!")
                p = int(input("p = "))
                
            q = int(input("q = "))
            while not mathsTools.isPrimeNumber(p):
                print("q must be a prime number!")
                q = int(input("q = "))
                
            N = p*q
        elif(int(choice)==2):
            N = int(input("N = "))
            p, q = mathsTools.findPQ(N)
            if(p==0 and q == 0):
                print("No valid values for p and q found.")
            else:
                print("p = "+str(p)+"\nq = "+str(q))
                validChoice = True
        
        
    φ = (p-1)*(q-1)
    
    print("φ = " + str(φ))

    
    E = int(input("E = "))
    while E>=φ or mathsTools.gcd(φ, E)!=1:
        print("E must be less than φ=" + str(φ) + " and gcd(φ, E) must be equal to 1.")
        E = int(input("E = "))
        
    
    D = mathsTools.modularMultiplicativeInverse(E, φ)

    print("The private key is " + str(D))
    
    return cryptString(M, N, E)

def cryptString(M, N, E):
    '''Takes in a string M and two numbers N and E, returns a string that is M coded.'''
    
    traduction = "" 

    for i in M:
        x = alphabet.index(i)
        
        if(x<10):
            traduction += "0" + str(x)
        else:
            traduction += str(x)

    C = "" 
    
    s, e = 0, 3
    while (s<len(traduction)):
        caractCode = crypt(int(traduction[s:e]), N, E)
        if(caractCode==-1):
            return -1;
        C += str(caractCode) + ";"
        s = e
        e += 3
        
    C = C[:-1]
    C += "."
    
    return C


def crypt(M, N, E):
    '''Takes in a string M and two numbers N and E, returns a string that is M coded.'''
    
    if(M>=N):
        return -1
    
    C = (M**E)%N
    
    return C


def decryptString(C, D, N):
    '''Takes in a string C and two numbers D and N, returns a string that is C decoded.'''
    
    traduction = ""
    buffer = "" 
    
    for i in C:
        if(i == ";"):
            z = decrypt(int(buffer), D, N)
            if(z<10):
                traduction += "00" + str(z)
            elif(z<100):
                traduction += "0" +str(z)
            else:
                traduction += str(z)
                
            buffer = ""
        elif(i == "."):
            z = decrypt(int(buffer), D, N)
            traduction += str(z)
            buffer = ""
        else:
            buffer += i
            
    M = ""
    s, e = 0, 2
    while (s<len(traduction)):
        M += alphabet[int(traduction[s:e])]
        s = e
        e += 2
        
    return M
        

def decrypt(C, D, N):
    '''Takes in a string C and two numbers D and N, returns a string that is C decoded.'''
    
    M = (C**D)%N
    
    return M


validChoice = False
while not validChoice:
    choice = input("1) Encoding a message\n2) Decoding a message\n--> ")
    if(int(choice)==1):
        M = input("Message --> ")
        C = prepaCrypt(M)
        if(C==-1):
            print("ERROR : Coding not possible")
        else:
            print("Coded message --> " + str(C))
        validChoice = True
        
    elif(int(choice)==2):
        C = input("Message --> ")
        D = int(input("Private key --> "))
        N = int(input("Public key (N) --> "))
        print("Decoded message --> " + str(decryptString(C, D, N)))
        validChoice = True

