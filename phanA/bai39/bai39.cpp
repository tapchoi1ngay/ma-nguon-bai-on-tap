#include <bits/stdc++.h>
using namespace std;

long long cach1(const vector<int>& a) {
    if (a.empty()) return 0;
    long long max_sum = a[0];
    for (size_t i = 0; i < a.size(); ++i) {
        for (size_t j = i; j < a.size(); ++j) {
            long long current_sum = 0;
            for (size_t k = i; k <= j; ++k) {
                current_sum += a[k];
            }
            max_sum = max(max_sum, current_sum);
        }
    }
    return max_sum;
}

long long cach2(const vector<int>& a) {
    if (a.empty()) return 0;
    long long max_sum = a[0];
    for (size_t i = 0; i < a.size(); ++i) {
        long long current_sum = 0;
        for (size_t j = i; j < a.size(); ++j) {
            current_sum += a[j];
            max_sum = max(max_sum, current_sum);
        }
    }
    return max_sum;
}

long long kadane(const vector<int>& a) {
    if (a.empty()) return 0;
    long long max_sum = a[0], current_sum = a[0];
    for (size_t i = 1; i < a.size(); ++i) {
        current_sum = max((long long)a[i], current_sum + a[i]);
        max_sum = max(max_sum, current_sum);
    }
    return max_sum;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        cout << kadane(a) << "\n";
    }
    return 0;
}
