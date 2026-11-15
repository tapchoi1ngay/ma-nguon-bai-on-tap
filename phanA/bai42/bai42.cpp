#include <bits/stdc++.h>
using namespace std;

pair<long long, int> cua_so_truot(const vector<int>& a, int k) {
    if (a.empty() || k <= 0 || k > (int)a.size()) return {0, 0};
    
    long long current_sum = 0;
    for (int i = 0; i < k; ++i) {
        current_sum += a[i];
    }
    
    long long max_sum = current_sum;
    int best_start = 1;
    
    for (int i = k; i < (int)a.size(); ++i) {
        current_sum = current_sum + a[i] - a[i - k];
        if (current_sum > max_sum) {
            max_sum = current_sum;
            best_start = i - k + 2; 
        }
    }
    return {max_sum, best_start};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    if (cin >> n >> k) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        
        pair<long long, int> kq = cua_so_truot(a, k);
        cout << "tong " << kq.first << ", bat dau tai vi tri " << kq.second << "\n";
    }
    return 0;
}
