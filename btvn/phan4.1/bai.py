import numpy as np

def knn_predict(X_train, y_train, x_query, k):
    distances = [np.sqrt(np.sum((np.array(x) - np.array(x_query))**2)) for x in X_train]
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = [y_train[i] for i in nearest_indices]
    return max(set(nearest_labels), key=nearest_labels.count)

X_train = [[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0]]
y_train = [0, 0, 1, 1, 0, 1]
x_query = [8.0, 9.0]
k = 3

predicted_label = knn_predict(X_train, y_train, x_query, k)
print(f"Voi diem x_query(8.0, 9.0), thuat toan KNN (K={k}) du doan nhan la: {predicted_label}")
