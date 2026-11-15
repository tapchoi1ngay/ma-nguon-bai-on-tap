#include <bits/stdc++.h>
using namespace std;

struct Mau { 
    vector<double> x; 
    string y; 
};

double do_chinh_xac_bo_mot_mau(const vector<Mau>& D, 
                               double (*kc)(const vector<double>&, const vector<double>&)) {
    int so_dung = 0;
    for (int i = 0; i < (int)D.size(); ++i) {
        double min_d = 1e18;
        string best_y = "";
        
        for (int j = 0; j < (int)D.size(); ++j) {
            if (i == j) continue; // Bỏ qua chính nó
            
            double dist = kc(D[i].x, D[j].x);
            if (dist < min_d) { 
                min_d = dist; 
                best_y = D[j].y; 
            }
        }
        
        if (best_y == D[i].y) {
            so_dung++;
        }
    }
    return (double)so_dung / D.size() * 100.0;
}

int main() {
    // Ham main de chay kiem thu
    return 0;
}
