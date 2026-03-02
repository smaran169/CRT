from typing import List

def Collatz_Sequence(n: int) -> List[int]:
    sequence = [n]  # start with the initial number
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

if __name__ == '__main__':
    n = int(input("Enter a positive integer: "))
    print(Collatz_Sequence(n))