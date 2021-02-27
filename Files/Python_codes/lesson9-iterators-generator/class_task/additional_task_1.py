def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def prime(xterms):
    i = 0
    n = 2

    while i <= xterms:
        if is_prime(n):
            yield n
            i+=1

        n+=1

prime = prime(10)
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
