import sys
input = sys.stdin.readline

def dem(a):
    chan = 0
    le = 0
    am = 0
    for x in a:
        if x < 0:
            am += 1
            
        if x % 2 == 0:
            chan += 1
        else:
            le += 1
            
    return (chan, le, am)

def main():
    line1 = input().strip()
    if not line1:
        return
    
    a = list(map(int, input().split()))
    
    chan, le, am = dem(a)
    print(f"chan {chan}, le {le}, am {am}")

main()
