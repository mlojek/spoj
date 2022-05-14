def factorial(n: int) -> int:
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


if __name__ == "__main__":
    loops = int(input())
    for _ in range(loops):
        n = int(input())
        print(factorial(n))