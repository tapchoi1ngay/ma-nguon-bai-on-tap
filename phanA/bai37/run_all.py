import os
import subprocess

print("ĐANG BIÊN DỊCH bai37.cpp...\n")
subprocess.run(["g++", "bai37.cpp", "-o", "bai37.exe"])

# Tạo 3 file test case
open('test1.txt', 'w').write("8\n3 -1 0 8 -7 5 -2 6\n")
open('test2.txt', 'w').write("3\n0 0 0\n")
open('test3.txt', 'w').write("4\n-2 -4 -6 -8\n")

print("KẾT QUẢ CHẠY 3 TEST BÀI 37:")
print("-" * 50)
for i in range(1, 4):
    print(f"--- TEST {i} ---")
    os.system(f"cmd /c \".\\bai37.exe < test{i}.txt\"")
print("-" * 50)
