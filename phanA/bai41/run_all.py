import os
import subprocess

print("ĐANG BIÊN DỊCH bai41.cpp...\n")
subprocess.run(["g++", "bai41.cpp", "-o", "bai41.exe"])

open('test1.txt', 'w').write("4\n2 3 -2 4\n")
open('test2.txt', 'w').write("3\n-2 0 -1\n")
open('test3.txt', 'w').write("3\n-2 3 -4\n")
open('test4.txt', 'w').write("5\n0 -3 0 -2 0\n")
open('test5.txt', 'w').write("5\n-1 -2 -3 0 1\n")
open('test6.txt', 'w').write("5\n2 -5 -2 -4 3\n")

print("KẾT QUẢ CHẠY 6 TEST BÀI 41:")
print("-" * 50)
for i in range(1, 7):
    print(f"--- TEST {i} ---")
    os.system(f"cmd /c \".\\bai41.exe < test{i}.txt\"")
print("-" * 50)
