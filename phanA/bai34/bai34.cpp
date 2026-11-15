#include <bits/stdc++.h>
using namespace std;

long long dao_nguoc(long long n) {
    long long rev = 0;
    long long abs_n = abs(n);
    
    while (abs_n > 0) {
        rev = rev * 10 + abs_n % 10;
        abs_n /= 10;
    }
    
    return n < 0 ? -rev : rev;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n;
    if (cin >> n) {
        cout << dao_nguoc(n) << "\n";
    }
    return 0;
}
