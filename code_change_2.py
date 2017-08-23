# Create a list with the first ten triangular numbers
# (see https://oeis.org/A000217)

L = [(i*(i+1))/2 for i in range(10)]

    



# Create a function to test if a number is prime
def is_prime(n):
        """
    Test if ``n`` is a prime.
    """
       
    for i in range(2,n):
        if (n%i==0):
            print "False"
            break
        if (i==n-1):
            print "True"


            # Tests
# is_prime(2033) == False
# is_prime(2039) == True

# Create a function which returns a list of the first ten prime numbers
# greater than or equal to n



def next_ten_primes(n):
    """
    Return the list of the first ten prime numbers greate than or equal to n
    """
    j=0
    P = []
    
    while (j<10):
        for i in range(2,n):
            if (n%i==0):
                n=n+1
                break
            
            if (i==n-1):
                
                P.append(n)
                n=n+1
                j=j+1

            
    print P
            
# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]






