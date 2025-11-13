# The idea behind is that the prime number is only number that is divisible by itself and 1 that's why
# we have taken all the prime and start divide by every element in the array so
# If remainder comes 0 then then the gcd is not 1
# If remainder comes 1 then then the gcd is 1
# and why we taken upto 53 because we can generate the 3.25 × 10¹⁸ = 2 × 3 × 5 × 7 × 11 × 13 × 17 × 19 × 23 × 29 × 31 × 37 × 41 × 43 × 47 × 53
# which is within constraint (10 ^ 18)

import sys
input = sys.stdin.readline


def solve():
    t = int(input())
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        for p in primes:
            ok = False
            for val in a:
                if val % p != 0:
                    ok = True
                    break
            if ok:
                print(p)
                break
        else:
            print(-1)


if __name__ == "__main__":
    solve()
