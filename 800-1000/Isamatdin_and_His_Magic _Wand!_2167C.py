# Idea behind that suppose if one odd or one even exists in the array
# then it is possible for creating a swap chain with others otherwise it is not possible
import sys
input = sys.stdin.readline


def solve():
    tests = int(input())
    for _ in range(tests):  # fixed loop
        n = int(input())
        nums = list(map(int, input().split()))

        c_even, c_odd = 0, 0
        for val in nums:
            if val % 2 == 0:
                c_even += 1
            else:
                c_odd += 1

            if c_even > 0 and c_odd > 0:
                print(*sorted(nums))
                break
        else:
            print(*nums)


if __name__ == "__main__":
    solve()
