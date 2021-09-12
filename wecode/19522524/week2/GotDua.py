def solve(n):
    if n <= 2:
        return "NO"
    if n % 2 == 0:
        return "YES"
    return "NO"

print(solve(int(input())))