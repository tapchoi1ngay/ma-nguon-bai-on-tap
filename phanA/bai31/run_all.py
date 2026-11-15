import os
import subprocess

# 1. Tự động sinh 4 file test vào thư mục bai31
open('test1.txt', 'w').write("7\n7 -3 12 0 5 -8 4\n")
open('test2.txt', 'w').write("1\n5\n")
open('test3.txt', 'w').write("4\n-2 -9 -3 -7\n")
open('test4.txt', 'w').write("1000000\n" + "1000000000 " * 1000000 + "\n")

print("ĐANG BIÊN DỊCH bai31.cpp...\n")
subprocess.run(["g++", "bai31.cpp", "-o", "bai31.exe"])

print("ĐANG CHẠY TOÀN BỘ 4 TEST...\n")
for i in range(1, 5):
    print(f"--- KẾT QUẢ TEST {i} ---")
    os.system(f"cmd /c \".\\bai31.exe < test{i}.txt\"")
    print("-" * 30 + "\n")
