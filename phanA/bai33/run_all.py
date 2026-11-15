import subprocess

print("ĐANG BIÊN DỊCH bai33.cpp...\n")
subprocess.run(["g++", "bai33.cpp", "-o", "bai33.exe"])

# 5 test case bắt buộc của Bài 33
tests = [
    "7",
    "100",
    "987654321",
    "1000000000",
    "1000000000000000000"
]

print("KẾT QUẢ CHẠY 5 TEST BÀI 33:")
print("-" * 50)
for t in tests:
    # Truyền trực tiếp từng con số vào chương trình C++
    result = subprocess.run([r".\bai33.exe"], input=t, text=True, capture_output=True)
    print(f"Đầu vào: {t:<20} | Kết quả in ra: {result.stdout.strip()}")
print("-" * 50)
