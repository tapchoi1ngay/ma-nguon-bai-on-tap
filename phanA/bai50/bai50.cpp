#include <bits/stdc++.h>
#include <chrono>
using namespace std;

struct Mau { vector<double> x; string y; };

void sinh_du_lieu(int n, int d, vector<Mau>& D, vector<vector<double>>& queries) {
    mt19937 rng(12345);
    uniform_real_distribution<double> dist(0.0, 10.0);
    
    D.resize(n);
    for (int i = 0; i < n; ++i) {
        D[i].x.resize(d);
        for (int j = 0; j < d; ++j) D[i].x[j] = dist(rng);
        D[i].y = "Lop" + to_string(i % 3);
    }
    
    int m = 1000;
    queries.resize(m, vector<double>(d));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < d; ++j) queries[i][j] = dist(rng);
    }
}

string lang_gieng_gan_nhat(const vector<double>& q, const vector<Mau>& D) {
    double min_d = 1e18;
    string best_y = "";
    for (int i = 0; i < (int)D.size(); ++i) {
        double dist = 0;
        for (size_t j = 0; j < q.size(); ++j) {
            dist += (q[j] - D[i].x[j]) * (q[j] - D[i].x[j]); // Khong can sqrt de toi uu toc do
        }
        if (dist < min_d) { min_d = dist; best_y = D[i].y; }
    }
    return best_y;
}

int main() {
    int n_arr[] = {1000, 10000, 100000};
    int d = 20;
    
    for (int n : n_arr) {
        vector<Mau> D;
        vector<vector<double>> queries;
        sinh_du_lieu(n, d, D, queries);
        
        auto t0 = chrono::steady_clock::now();
        for (const auto& q : queries) {
            lang_gieng_gan_nhat(q, D);
        }
        auto t1 = chrono::steady_clock::now();
        
        double giay = chrono::duration<double>(t1 - t0).count();
        cout << "n = " << n << " -> " << fixed << setprecision(4) << giay << " giay\n";
    }
    return 0;
}
