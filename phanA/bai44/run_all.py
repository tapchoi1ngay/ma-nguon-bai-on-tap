import os
import subprocess
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Vui long chay lenh: pip install matplotlib de ve do thi")
    exit()

print("ĐANG BIÊN DỊCH bai44.cpp...\n")
subprocess.run(["g++", "bai44.cpp", "-o", "bai44.exe"])

ns = [500, 1000, 2000, 4000]
python_times = []

print("KẾT QUẢ ĐO THỜI GIAN PYTHON:")
print("-" * 50)
for n in ns:
    result = subprocess.run(["python", "bai44.py"], input=str(n), text=True, capture_output=True)
    t = float(result.stdout.strip())
    python_times.append(t)
    print(f"n = {n:<5} -> {t:.6f} giay")
print("-" * 50)

# Vẽ đồ thị
plt.figure(figsize=(8, 5))
plt.plot(ns, python_times, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
plt.title("Đoạn thực nghiệm thời gian chạy của thuật toán O(n^2) - Python")
plt.xlabel("Kích thước đầu vào (n)")
plt.ylabel("Thời gian chạy tối thiểu (giây)")
plt.grid(True, linestyle='--', alpha=0.7)

# Ghi chú giá trị lên đồ thị
for i, txt in enumerate(python_times):
    plt.annotate(f"{txt:.3f}s", (ns[i], python_times[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.savefig("dothi_On2.png", dpi=300, bbox_inches='tight')
print("\nĐã vẽ thành công! Hãy mở file 'dothi_On2.png' trong thư mục để chèn vào Word.")
