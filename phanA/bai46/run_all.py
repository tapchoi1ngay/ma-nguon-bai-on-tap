import os
import subprocess

print("ĐANG BIÊN DỊCH bai46.cpp...\n")
subprocess.run(["g++", "bai46.cpp", "-o", "bai46.exe"])

# Tạo file dataset nhúng sẵn 7 mẫu và 4 truy vấn
dataset = """7 2
1.4 0.2 Setosa
0.0 0.0 Dummy
0.0 0.0 Dummy
4.8 1.3 Versicolor
0.0 0.0 Dummy
4.9 1.5 Versicolor
6.0 2.1 Virginica
4
4.8 1.4
1.4 0.2
6.1 2.3
5.0 1.8
"""
open('dataset.txt', 'w').write(dataset)

print("KẾT QUẢ CHẠY 4 TRUY VẤN BÀI 46 (C++):")
print("-" * 50)
os.system("cmd /c \".\\bai46.exe < dataset.txt\"")
print("-" * 50)
