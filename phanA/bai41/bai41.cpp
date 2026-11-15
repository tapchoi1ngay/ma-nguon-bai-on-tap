#include <bits/stdc++.h>
using namespace std;

long long tich_lon_nhat(const vector<int>& a) {
    if (a.empty()) return 0;
    long long max_val = a[0], min_val = a[0], best = a[0];
    
    for (size_t i = 1; i < a.size(); ++i) {
        if (a[i] < 0) swap(max_val, min_val);
        max_val = max((long long)a[i], max_val * a[i]);
        min_val = min((long long)a[i], min_val * a[i]);
        best = max(best, max_val);
    }
    return best;
}

long long tich_lon_nhat_n2(const vector<int>& a) {
    if (a.empty()) return 0;
    long long best = a[0];
    for (size_t i = 0; i < a.size(); ++i) {
        long long current = 1;
        for (size_t j = i; j < a.size(); ++j) {
            current *= a[j];
            best = max(best, current);
        }
    }
    return best;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        cout << tich_lon_nhat(a) << "\n";
    }
    return 0;
}
