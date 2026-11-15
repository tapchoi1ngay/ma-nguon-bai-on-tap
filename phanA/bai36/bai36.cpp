#include <bits/stdc++.h>
using namespace std;

// tra ve false neu tran
bool giai_thua(int n, long long &kq) {
    kq = 1;
    for (int i = 1; i <= n; ++i) {
        // kiem tra kq > LLONG_MAX / i truoc khi nhan
        if (kq > LLONG_MAX / i) {
            return false;
        }
        kq *= i;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (cin >> n) {
        long long kq;
        if (giai_thua(n, kq)) {
            cout << kq << "\n";
        } else {
            cout << "TRAN SO\n";
        }
    }
    return 0;
}
