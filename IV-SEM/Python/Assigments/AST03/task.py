def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    # Calculate average
    average = (n1 + n2 + n3) / 3

    # Determine status
    status = "Pass" if average >= 40 else "Fail"

    # Format output
    return f"Average grade: {average:.2f}, Status: {status}"


if __name__ == '__main__':
    name = input().strip()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))