#include <bits/stdc++.h>
using namespace std;

bool la_nguyen_to(int n) {
    if (n < 2) return false;
    for (long long i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

vector<int> sang_eratosthenes(int n) {
    vector<bool> is_prime(n + 1, true);
    if (n >= 0) is_prime[0] = false;
    if (n >= 1) is_prime[1] = false;
    
    for (long long i = 2; i * i <= n; ++i) {
        if (is_prime[i]) {
            for (long long j = i * i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    
    vector<int> primes;
    for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) primes.push_back(i);
    }
    return primes;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (cin >> n) {
        vector<int> primes = sang_eratosthenes(n);
        
        if (n <= 30) {
            for (int p : primes) cout << p << " ";
            cout << " (" << primes.size() << " so)\n";
        } else if (n < 1000000) {
            cout << "so luong = " << primes.size() << "\n";
        } else {
            long long tong = 0;
            for (int p : primes) tong += p;
            cout << "so luong = " << primes.size() << ", tong = " << tong << "\n";
        }
    }
    return 0;
}
