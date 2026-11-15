import os
import subprocess

print("ĐANG BIÊN DỊCH bai42.cpp...\n")
subprocess.run(["g++", "bai42.cpp", "-o", "bai42.exe"])

open('test1.txt', 'w').write("9 4\n1 4 2 10 2 3 1 0 20\n")
open('test2.txt', 'w').write("4 2\n-3 -1 -4 -1\n")
open('test3.txt', 'w').write("3 3\n5 5 5\n")

print("KẾT QUẢ CHẠY 3 TEST BÀI 42:")
print("-" * 50)
for i in range(1, 4):
    print(f"--- TEST {i} ---")
    os.system(f"cmd /c \".\\bai42.exe < test{i}.txt\"")
print("-" * 50)
