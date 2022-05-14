def derivative(sequence: list, new: int) -> list:
    if len(sequence) == 1:
        return [sequence[0]] * new
    else:
        # Run recursive function:
        d_sequence = []
        for i in range(len(sequence) - 1):
            d_sequence.append(sequence[i+1] - sequence[i])

        d_next = derivative(d_sequence, new)

        # Generate new elements:
        next = []
        next.append(sequence[-1] + d_next[0])
        for i in range(1, new):
            next.append(next[i-1] + d_next[i])

        # Return new values:
        return next


if __name__ == "__main__":
    loops = int(input())
    for _ in range(loops):
        length, new = [int(i) for i in input().split()]
        sequence = [int(i) for i in input().split()]
        for i in derivative(sequence, new):
            print(i, end=' ')
        print()