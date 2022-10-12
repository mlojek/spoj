if __name__ == "__main__":
    # loop for 10 test cases
    for _ in range(10):
        sum_apples = int(input())
        difference = int(input())
        
        natalia = (sum_apples - difference) // 2
        klaudia = natalia + difference

        print(klaudia)
        print(natalia)