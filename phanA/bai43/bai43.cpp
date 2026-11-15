#include <bits/stdc++.h>
using namespace std;

long long dem = 0;

long long fib_de_quy(int n) {
    dem++;
    if (n <= 1) return n;
    return fib_de_quy(n - 1) + fib_de_quy(n - 2);
}

long long fib_ghi_nho_helper(int n, vector<long long>& memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fib_ghi_nho_helper(n - 1, memo) + fib_ghi_nho_helper(n - 2, memo);
}

long long fib_ghi_nho(int n) {
    vector<long long> memo(n + 1, -1);
    return fib_ghi_nho_helper(n, memo);
}

long long fib_lap(int n) {
    if (n <= 1) return n;
    long long f0 = 0, f1 = 1, fn = 0;
    for (int i = 2; i <= n; ++i) {
        if (LLONG_MAX - f1 < f0) {
            return -1; // Tra ve -1 de bao loi tran so
        }
        fn = f0 + f1;
        f0 = f1;
        f1 = fn;
    }
    return fn;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (cin >> n) {
        if (n <= 30) {
            dem = 0;
            long long f = fib_de_quy(n);
            cout << "F = " << f << ", so loi goi = " << dem << "\n";
        } else {
            long long f = fib_lap(n);
            if (f == -1) cout << "tran long long\n";
            else cout << "F = " << f << "\n";
        }
    }
    return 0;
}
