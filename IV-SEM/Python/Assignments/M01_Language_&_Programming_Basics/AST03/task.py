import math

def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    
    avg = (n1 + n2 + n3) / 3
    
    avg_truncated = math.floor(avg * 100) / 100
    
    avg_str = f"{avg_truncated:.1f}" if avg_truncated.is_integer() else f"{avg_truncated:.2f}"
    
    status = "Pass" if avg_truncated >= 40 else "fail"
    return f"Average grade: {avg_str}, Status: {status}"


if __name__ == '__main__':
    name = input().strip()
    n1, n2, n3 = map(int, input().split())
    print(Student_Grade_System(name, n1, n2, n3))