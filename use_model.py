# Import thư viện cần thiết
import joblib

# Tải mô hình đã lưu
loaded_model = joblib.load('model.pkl')

# Dữ liệu kiểm tra
X_test = ["I enjoy learning about AI."]

# Dự đoán với mô hình đã tải
predictions = loaded_model.predict(X_test)

# In kết quả dự đoán
print("Predictions:", predictions)
