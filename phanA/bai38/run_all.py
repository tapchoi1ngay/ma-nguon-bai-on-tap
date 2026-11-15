import os
import subprocess

print("ĐANG BIÊN DỊCH bai38.cpp...\n")
subprocess.run(["g++", "bai38.cpp", "-o", "bai38.exe"])

open('test1.txt', 'w').write("5\n1 2 2 5 9\n")
open('test2.txt', 'w').write("3\n1 3 2\n")
open('test3.txt', 'w').write("1\n5\n")
open('test4.txt', 'w').write("3\n2 2 2\n")

print("KẾT QUẢ CHẠY 4 TEST BÀI 38:")
print("-" * 50)
for i in range(1, 5):
    print(f"--- TEST {i} ---")
    os.system(f"cmd /c \".\\bai38.exe < test{i}.txt\"")
print("-" * 50)
