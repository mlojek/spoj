def is_prime(number: int):
    if number < 2:
        return False
    else:
        i = 2
        while i*i <= number:
            if number % i == 0:
                return False
            i += 1
    return True


if __name__ == "__main__":
    loops = int(input())
    for _ in range(loops):
        first, last = (int(i) for i in input().split())
        for i in range(first, last + 1):
            if is_prime(i):
                print(i)
        print()

# Time limit exceeded!