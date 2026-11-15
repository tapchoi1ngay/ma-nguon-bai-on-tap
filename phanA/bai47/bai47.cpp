#include <bits/stdc++.h>
using namespace std;

struct Mau { 
    vector<double> x; 
    string y; 
};

struct KetQua { 
    string nhan; 
    double khoang_cach; 
    int chi_so; 
};

vector<Mau> doc_du_lieu(const string& ten_tep, int &d) {
    ifstream fin(ten_tep);
    vector<Mau> D;
    if (!fin.is_open()) return D;
    
    int n;
    if (fin >> n >> d) {
        for (int i = 0; i < n; ++i) {
            Mau m;
            m.x.resize(d);
            for (int j = 0; j < d; ++j) {
                fin >> m.x[j];
            }
            fin >> m.y;
            D.push_back(m);
        }
    }
    return D;
}

KetQua lang_gieng_gan_nhat(const vector<double>& q, const vector<Mau>& D) {
    double min_d = 1e18;
    string best_y = "";
    int best_idx = -1;
    
    for (int i = 0; i < (int)D.size(); ++i) {
        double dist = 0;
        for (size_t j = 0; j < q.size(); ++j) {
            dist += (q[j] - D[i].x[j]) * (q[j] - D[i].x[j]);
        }
        dist = sqrt(dist);
        
        if (dist < min_d) { 
            min_d = dist; 
            best_y = D[i].y; 
            best_idx = i + 1; // Đánh số từ 1
        }
    }
    return {best_y, min_d, best_idx};
}

int main() {
    int d;
    vector<Mau> D = doc_du_lieu("dataset.txt", d);
    if (D.empty()) {
        cout << "Khong doc duoc du lieu!\n";
        return 0;
    }
    
    // 5 truy van theo yeu cau de bai
    vector<vector<double>> queries = {
        {4.9, 3.3, 1.5, 0.2}, 
        {6.1, 2.8, 4.7, 1.2}, 
        {6.5, 3.0, 5.5, 2.0}, 
        {5.9, 3.0, 4.8, 1.8}, 
        {6.0, 2.7, 5.1, 1.6}
    };
    
    for (auto& q : queries) {
        KetQua kq = lang_gieng_gan_nhat(q, D);
        cout << kq.nhan << " -- mau " << kq.chi_so << ", khoang cach " 
             << fixed << setprecision(4) << kq.khoang_cach << "\n";
    }
    return 0;
}
