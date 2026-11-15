#include <bits/stdc++.h>
#include <chrono>
using namespace std;

long long thuat_toan_On2(int n) {
    long long tong = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            tong += (i * j);
        }
    }
    return tong;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (cin >> n) {
        double min_time = 1e9;
        for(int lap = 0; lap < 3; lap++) {
            auto t0 = chrono::steady_clock::now();
            thuat_toan_On2(n);
            auto t1 = chrono::steady_clock::now();
            
            double giay = chrono::duration<double>(t1 - t0).count();
            min_time = min(min_time, giay);
        }
        cout << fixed << setprecision(6) << min_time << "\n";
    }
    return 0;
}
