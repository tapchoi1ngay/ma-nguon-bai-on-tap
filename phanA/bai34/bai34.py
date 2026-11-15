import sys
input = sys.stdin.readline

def dao_nguoc(n: int) -> int:
    rev = 0
    abs_n = abs(n)
    
    while abs_n > 0:
        rev = rev * 10 + abs_n % 10
        abs_n //= 10
        
    return -rev if n < 0 else rev

def main():
    line = input().strip()
    if not line:
        return
    n = int(line)
    print(dao_nguoc(n))

main()
