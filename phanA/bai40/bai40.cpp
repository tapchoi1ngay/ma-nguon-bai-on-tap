#include <bits/stdc++.h>
using namespace std;

struct KetQua { long long tong; int dau, cuoi; };

KetQua kadane_chi_so(const vector<int>& a) {
    if (a.empty()) return {0, 0, 0};
    long long max_sum = a[0], current_sum = a[0];
    int best_start = 0, best_end = 0, current_start = 0;
    
    for (int i = 1; i < (int)a.size(); ++i) {
        if (a[i] > current_sum + a[i]) {
            current_sum = a[i];
            current_start = i;
        } else {
            current_sum += a[i];
        }
        
        if (current_sum > max_sum) {
            max_sum = current_sum;
            best_start = current_start;
            best_end = i;
        }
    }
    // Cong 1 de hien thi theo chuan danh so tu 1
    return {max_sum, best_start + 1, best_end + 1};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        KetQua kq = kadane_chi_so(a);
        cout << "tong " << kq.tong << ", doan [" << kq.dau << ".." << kq.cuoi << "]\n";
    }
    return 0;
}
