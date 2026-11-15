import os
import subprocess

print("ĐANG BIÊN DỊCH bai43.cpp...\n")
subprocess.run(["g++", "bai43.cpp", "-o", "bai43.exe"])

# Tạo 5 test case đúng theo yêu cầu của đề
tests = ["10", "20", "30", "92", "93"]

print("KẾT QUẢ CHẠY 5 TEST BÀI 43:")
print("-" * 50)
for t in tests:
    # Ghi nội dung vào file test.txt
    with open('test.txt', 'w') as f:
        f.write(t + "\n")
    
    print(f"--- TEST n = {t} ---")
    os.system(f"cmd /c \".\\bai43.exe < test.txt\"")
print("-" * 50)
