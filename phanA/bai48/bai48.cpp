#include <bits/stdc++.h>
using namespace std;

struct Mau { 
    vector<double> x; 
    string y; 
};

double kc_euclid(const vector<double>& u, const vector<double>& v) {
    double d = 0;
    for (size_t i = 0; i < u.size(); ++i) {
        d += (u[i] - v[i]) * (u[i] - v[i]);
    }
    return sqrt(d);
}

double kc_manhattan(const vector<double>& u, const vector<double>& v) {
    double d = 0;
    for (size_t i = 0; i < u.size(); ++i) {
        d += abs(u[i] - v[i]);
    }
    return d;
}

void lang_gieng_gan_nhat(const vector<double>& q, const vector<Mau>& D, 
                         double (*kc)(const vector<double>&, const vector<double>&)) {
    double min_d = 1e18;
    int best_idx = -1;
    for (int i = 0; i < (int)D.size(); ++i) {
        double dist = kc(q, D[i].x);
        if (dist < min_d) { 
            min_d = dist; 
            best_idx = i + 1; 
        }
    }
    cout << "mau " << best_idx << "\n";
}

int main() {
    // Ham main de chay kiem thu thuat toan
    return 0;
}
