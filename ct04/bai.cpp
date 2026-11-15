#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int n_size, nodes = 0, sols = 0;
vector<int> x;

bool is_safe(int r, int c) {
    for (int i = 1; i < r; ++i) {
        if (x[i] == c || abs(x[i] - c) == abs(i - r)) return false;
    }
    return true;
}

void try_queen(int i) {
    nodes++; // Đếm 1 nút mỗi khi gọi hàm đệ quy
    
    for (int j = 1; j <= n_size; ++j) {
        if (is_safe(i, j)) {
            x[i] = j;
            if (i == n_size) {
                sols++;
                if (sols == 1) {
                    cout << "Loi giai 1: ";
                    for(int k = 1; k <= n_size; k++) cout << x[k] << " ";
                    cout << "\n";
                }
            } else {
                try_queen(i + 1);
            }
        }
    }
}

int main() {
    cout << "Nhap n: ";
    cin >> n_size;
    x.resize(n_size + 1); // Cấp phát để dùng chỉ số từ 1 đến n
    try_queen(1);
    cout << "Nodes: " << nodes << ", Sols: " << sols << endl;
    return 0;
}
