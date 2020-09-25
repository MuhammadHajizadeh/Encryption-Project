# use Python 3 print function
# this allows this code to run on python 2.x and 3.x
from __future__ import print_function

def power(x, y, p):
    res = 1  # Initialize result

    # Update x if it is more
    # than or equal to p
    x = x % p

    if (x == 0):
        return 0

    while (y > 0):

        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1):
            res = (res * x) % p

            # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


# Variables Used
sharedPrime = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919  # p
sharedBase = 2  # g

aliceSecret = 1101001010019203192312312312435234234131235457686756554434232325365645342323243  # a
bobSecret = 2343423432473984729384792837492837498273984739847982  # b

# Begin
print("Publicly Shared Variables:")
print("    Publicly Shared Prime: ", sharedPrime)
print("    Publicly Shared Base:  ", sharedBase)

# Alice Sends Bob A = g^a mod p
A = power(sharedBase, aliceSecret, sharedPrime)
print("\n  Alice Sends Over Public Chanel: ", A)

# Bob Sends Alice B = g^b mod px
B = power(sharedBase, bobSecret, sharedPrime)


print("Privately Calculated Shared Secret:")
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = power(B, aliceSecret, sharedPrime)
print("Alice Shared Secret: ", aliceSharedSecret)

# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = power(A, aliceSecret, sharedPrime)
print("Bob Shared Secret: ", bobSharedSecret)


