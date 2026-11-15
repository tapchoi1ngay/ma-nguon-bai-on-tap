import os
import subprocess

print("ĐANG BIÊN DỊCH bai40.cpp...\n")
subprocess.run(["g++", "bai40.cpp", "-o", "bai40.exe"])

open('test1.txt', 'w').write("8\n4 -3 5 -2 -1 2 6 -9\n")
open('test2.txt', 'w').write("3\n-5 -2 -9\n")
open('test3.txt', 'w').write("9\n-2 1 -3 4 -1 2 1 -5 4\n")
open('test4.txt', 'w').write("4\n1 2 3 4\n")

print("KẾT QUẢ CHẠY 4 TEST BÀI 40:")
print("-" * 50)
for i in range(1, 5):
    print(f"--- TEST {i} ---")
    os.system(f"cmd /c \".\\bai40.exe < test{i}.txt\"")
print("-" * 50)
