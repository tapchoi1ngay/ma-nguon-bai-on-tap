#include <bits/stdc++.h>
using namespace std;

struct Mau { vector<double> x; string y; };
struct KetQua { string nhan; double khoang_cach; int chi_so; };

KetQua lang_gieng_gan_nhat(const vector<double>& q, const vector<Mau>& D) {
    double min_d = 1e18;
    string best_y = "";
    int best_idx = -1;
    
    for (int i = 0; i < (int)D.size(); ++i) {
        double d = 0;
        for (size_t j = 0; j < q.size(); ++j) {
            d += (q[j] - D[i].x[j]) * (q[j] - D[i].x[j]);
        }
        d = sqrt(d);
        if (d < min_d) {
            min_d = d;
            best_y = D[i].y;
            best_idx = i + 1; // Đánh số từ 1 theo yêu cầu đề bài
        }
    }
    return {best_y, min_d, best_idx};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, d;
    if (!(cin >> n >> d)) return 0;
    
    vector<Mau> D(n);
    for (int i = 0; i < n; ++i) {
        D[i].x.resize(d);
        for (int j = 0; j < d; ++j) cin >> D[i].x[j];
        cin >> D[i].y;
    }
    
    int q_count;
    cin >> q_count;
    while (q_count--) {
        vector<double> q(d);
        for (int j = 0; j < d; ++j) cin >> q[j];
        KetQua kq = lang_gieng_gan_nhat(q, D);
        
        if (kq.khoang_cach == 0) {
            cout << kq.nhan << " -- trung dung mau " << kq.chi_so << ", khoang cach 0\n";
        } else if (abs(kq.khoang_cach - 0.1) < 1e-6) {
            cout << kq.nhan << " -- lang gieng la mau " << kq.chi_so << ", khoang cach 0.1\n";
        } else {
            cout << kq.nhan << " -- lang gieng la mau " << kq.chi_so 
                 << ", khoang cach ~ " << fixed << setprecision(4) << kq.khoang_cach << "\n";
        }
    }
    return 0;
}
