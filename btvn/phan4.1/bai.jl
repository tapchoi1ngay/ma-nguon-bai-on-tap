using Distances

function knn_predict(X_train, y_train, x_query, k)
    distances = [euclidean(x, x_query) for x in X_train]
    nearest_indices = sortperm(distances)[1:k]
    nearest_labels = y_train[nearest_indices]
    
    counts = Dict()
    for label in nearest_labels
        counts[label] = get(counts, label, 0) + 1
    end
    return argmax(counts)
end

X_train = [[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0]]
y_train = [0, 0, 1, 1, 0, 1]
x_query = [8.0, 9.0]
k = 3

predicted_label = knn_predict(X_train, y_train, x_query, k)
println("Voi diem x_query(8.0, 9.0), thuat toan KNN (K=$k) du doan nhan la: $predicted_label")
