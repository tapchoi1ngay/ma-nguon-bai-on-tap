#include <iostream>
#include <vector>
using namespace std;

int n_val, so_loi_giai, so_nut;
vector<int> x, loi_giai_dau_tien;
vector<bool> cot, cheo1, cheo2;

void dat(int i) {
    so_nut++;
    if (i > n_val) {
        so_loi_giai++;
        if (loi_giai_dau_tien.empty()) loi_giai_dau_tien = x;
        return;
    }
    for (int j = 1; j <= n_val; j++) {
        if (!cot[j] && !cheo1[i + j] && !cheo2[i - j + n_val]) {
            x[i] = j;
            cot[j] = cheo1[i + j] = cheo2[i - j + n_val] = true;
            dat(i + 1);
            cot[j] = cheo1[i + j] = cheo2[i - j + n_val] = false;
        }
    }
}

void solve_for_n(int n) {
    n_val = n;
    so_loi_giai = 0;
    so_nut = 0;
    loi_giai_dau_tien.clear();
    
    x.assign(n + 1, 0);
    cot.assign(n + 1, false);
    cheo1.assign(2 * n + 1, false);
    cheo2.assign(2 * n + 1, false);
    
    dat(1);
    
    cout << "--- KET QUA CHO n = " << n << " ---\n";
    cout << "So nut da duyet: " << so_nut << "\n";
    cout << "So loi giai: " << so_loi_giai << "\n";
    if (!loi_giai_dau_tien.empty()) {
        cout << "Ban co loi giai dau tien:\n";
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cout << (loi_giai_dau_tien[i] == j ? "Q " : ". ");
            }
            cout << "\n";
        }
    }
    cout << "\n";
}

int main() {
    cout << "N24DCDT090 LeVoDatThoi\n\n";
    
    int test_cases[] = {5, 6, 8};
    for (int n : test_cases) {
        solve_for_n(n);
    }
    return 0;
}
