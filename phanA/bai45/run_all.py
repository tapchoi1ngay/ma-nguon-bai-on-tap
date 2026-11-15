import os
import subprocess

print("ĐANG BIÊN DỊCH bai45.cpp...\n")
subprocess.run(["g++", "bai45.cpp", "-o", "bai45.exe"])

open('test1.txt', 'w').write("2 10 1000\n")
open('test2.txt', 'w').write("3 1000000000000000000 1000000007\n")
open('test3.txt', 'w').write("2 1000000000000000000 1000000007\n")
open('test4.txt', 'w').write("123456789 987654321 1000000007\n")
open('test5.txt', 'w').write("5 0 7\n")
open('test6.txt', 'w').write("7 1 1\n")

print("KẾT QUẢ CHẠY 6 TEST BÀI 45:")
print("-" * 50)
for i in range(1, 7):
    print(f"--- TEST {i} ---")
    os.system(f"cmd /c \".\\bai45.exe < test{i}.txt\"")
print("-" * 50)
