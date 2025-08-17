def gcd(a,b):
    mini = min(a,b)
    for i in range(mini,0,-1):
        if a%i==0 and b%i==0:
            return i

def lcm(a,b):
    gcds = gcd(a,b)
    return (a*b)//gcds

def is_prime(n):
    if n==0 or n==1:
        return False 
    if n==2 or n==3:
        return True
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True