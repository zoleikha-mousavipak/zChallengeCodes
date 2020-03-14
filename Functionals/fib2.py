def zfib(n):
    if n <= 1:
        return n
    return zfib(n-1)+zfib(n-2)


if __name__ == "__main__":
    inp = int(input("N: "))
    for i in range(inp):
        print(zfib(i))