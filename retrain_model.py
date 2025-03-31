# Import các thư viện cần thiết
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Dữ liệu huấn luyện ví dụ
X_train = ["This is a good example.", "I love machine learning.", "Text classification is fun."]
y_train = [1, 1, 0]  # 1 = tích cực, 0 = tiêu cực

# Xây dựng pipeline với CountVectorizer và MultinomialNB
model = Pipeline([
    ('vectorizer', CountVectorizer()),  # Chuyển văn bản thành vector
    ('classifier', MultinomialNB())     # Sử dụng Naive Bayes cho phân loại
])

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Lưu mô hình đã huấn luyện
joblib.dump(model, 'text.pkl')
print("Model has been trained and saved.")
