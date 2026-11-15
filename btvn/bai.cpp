#include <iostream>
#include <vector>
using namespace std;

void insertionSort(vector<int>& A) {
    int n = A.size();
    for(int i = 1; i < n; i++) {
        int x = A[i];
        int j = i - 1;
        while(j >= 0 && A[j] > x) {
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = x;
    }
}

int main() {
    vector<int> A = {8, 3, 5, 1, 9, 2};
    insertionSort(A);
    for(int i : A) cout << i << " ";
    return 0;
}
