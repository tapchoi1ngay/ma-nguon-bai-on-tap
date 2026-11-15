#include <bits/stdc++.h>
using namespace std;

long long luy_thua_mod(long long a, long long b, long long m) {
    long long r = 1 % m; 
    a %= m;
    while (b > 0) {
        if (b % 2 == 1) {
            r = (r * a) % m;
        }
        a = (a * a) % m;
        b /= 2;
    }
    return r;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long a, b, m;
    if (cin >> a >> b >> m) {
        cout << luy_thua_mod(a, b, m) << "\n";
    }
    return 0;
}
