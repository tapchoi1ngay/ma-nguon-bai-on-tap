#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;

int knn_predict(vector<vector<double>>& X_train, vector<int>& y_train, vector<double>& x_query, int k) {
    int n = X_train.size();
    vector<pair<double, int>> dist_idx;
    
    for(int i = 0; i < n; ++i) {
        double dist = 0;
        for(size_t j = 0; j < x_query.size(); ++j) {
            dist += pow(X_train[i][j] - x_query[j], 2);
        }
        dist_idx.push_back({sqrt(dist), y_train[i]});
    }
    
    sort(dist_idx.begin(), dist_idx.end());

    map<int, int> counts;
    for(int i = 0; i < k; i++) {
        counts[dist_idx[i].second]++;
    }

    int best_label = -1;
    int max_count = -1;
    for(auto const& pair : counts) {
        if(pair.second > max_count) {
            max_count = pair.second;
            best_label = pair.first;
        }
    }
    return best_label;
}

int main() {
    vector<vector<double>> X_train = {
        {1.0, 2.0}, {1.5, 1.8}, {5.0, 8.0}, {8.0, 8.0}, {1.0, 0.6}, {9.0, 11.0}
    };
    vector<int> y_train = {0, 0, 1, 1, 0, 1};
    vector<double> x_query = {8.0, 9.0};
    int k = 3;

    int predicted_label = knn_predict(X_train, y_train, x_query, k);
    cout << "Voi diem x_query(8.0, 9.0), thuat toan KNN (K=" << k << ") du doan nhan la: " << predicted_label << endl;

    return 0;
}
