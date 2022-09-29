"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes>0:
        i = 0
        prime = 2
        while i<number_of_primes:
            if checkPrime(prime):
                list.insert(i, prime)
                prime+=1
                i+=1
            else:
                prime+=1
    elif number_of_primes<=0:
        raise ValueError(f"{number_of_primes} is smaller than 1")

    return list

def checkPrime(prime):
    isPrime = True
    for p in range(2, prime):
        if (prime%p) == 0:
            isPrime = False
    return isPrime
