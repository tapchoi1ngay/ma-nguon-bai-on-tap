import subprocess

print("ĐANG BIÊN DỊCH bai34.cpp...\n")
subprocess.run(["g++", "bai34.cpp", "-o", "bai34.exe"])

# 5 test case bắt buộc của Bài 34
tests = [
    "12345",
    "1000",
    "7",
    "-123",
    "2147483647"
]

print("KẾT QUẢ CHẠY 5 TEST BÀI 34:")
print("-" * 50)
for t in tests:
    # Truyền trực tiếp từng con số vào chương trình C++
    result = subprocess.run([r".\bai34.exe"], input=t, text=True, capture_output=True)
    print(f"Đầu vào: {t:<15} | Kết quả in ra: {result.stdout.strip()}")
print("-" * 50)
