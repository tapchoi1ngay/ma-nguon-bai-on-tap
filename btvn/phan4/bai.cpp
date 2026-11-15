#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void twoPointersSum(vector<int>& A, int S) {
    sort(A.begin(), A.end());
    int L = 0, R = A.size() - 1;
    while(L < R) {
        if(A[L] + A[R] == S) {
            cout << "Found: " << A[L] << " and " << A[R] << endl;
            return;
        } else if (A[L] + A[R] < S) {
            L++;
        } else {
            R--;
        }
    }
    cout << "Not found" << endl;
}

int main() {
    vector<int> A = {8, 3, 5, 1, 9, 2};
    int S = 8;
    twoPointersSum(A, S);
    return 0;
}
