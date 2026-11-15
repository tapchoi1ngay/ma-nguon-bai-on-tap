#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    long long tong = 0;
    int nho_nhat, lon_nhat;
    
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        if (i == 0) {
            nho_nhat = lon_nhat = x;
        } else {
            if (x < nho_nhat) nho_nhat = x;
            if (x > lon_nhat) lon_nhat = x;
        }
        tong += x;
    }
    
    double trung_binh = (double)tong / n;
    
    cout << tong << " ";
    cout << fixed << setprecision(4) << trung_binh << " ";
    cout << nho_nhat << " " << lon_nhat << "\n";
    
    return 0;
}
