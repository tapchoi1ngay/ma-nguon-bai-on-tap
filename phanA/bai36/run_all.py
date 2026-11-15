import subprocess

print("ĐANG BIÊN DỊCH bai36.cpp...\n")
subprocess.run(["g++", "bai36.cpp", "-o", "bai36.exe"])

# 4 test case bắt buộc của Bài 36
tests = ["0", "5", "20", "21"]

print("1. KẾT QUẢ CHẠY C++ (Có báo tràn số):")
for t in tests:
    result = subprocess.run([r".\bai36.exe"], input=t, text=True, capture_output=True)
    print(f"n = {t:<2} | {result.stdout.strip()}")

print("\n2. KẾT QUẢ CHẠY PYTHON (Không giới hạn, không tràn):")
for t in tests:
    result = subprocess.run(["python", "bai36.py"], input=t, text=True, capture_output=True)
    print(f"n = {t:<2} | {result.stdout.strip()}")
