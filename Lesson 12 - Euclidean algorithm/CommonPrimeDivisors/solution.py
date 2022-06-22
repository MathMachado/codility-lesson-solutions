# Code written in Python
# Correctness: 100 %
# Performance: 100 %
# Time Complexity: O(Z * log(max(A) + max(B))^2)
# Space Complexity: O(1)

def solution(A, B):
    Z = len(A)

    return sum(bool(commonPrimeDivisors(A[i], B[i])) for i in xrange(Z))


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def commonPrimeDivisors(a, b):
    ab_gcd = gcd(a, b)

    while a != 1:
        a_gcd = gcd(a, ab_gcd )

        if a_gcd == 1:
            break

        a /= a_gcd

    if a != 1:
        return False

    while b != 1:
        b_gcd = gcd(b, ab_gcd )
        
        if b_gcd == 1:
            break

        b /= b_gcd

    if b != 1:
        return False
        
    return True
