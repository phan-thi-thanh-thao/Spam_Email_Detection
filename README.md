# Email Spam Detection Web Application with Machine Learning

This web application provides real-time email classification to detect spam messages using machine learning. It offers a user-friendly interface where users can paste email content or upload files for instant spam analysis, with visual feedback and exportable reports.

The application uses a Naive Bayes classifier trained on text data to determine whether an email is spam or legitimate (ham). It supports multiple input formats including plain text, .eml, .doc, and .docx files, making it versatile for different email sources. The results are presented with interactive visual elements and can be exported to Word documents for documentation and sharing.

## Repository Structure
```
.
├── main.py                 # Flask application entry point with routing and core logic
├── retrain_model.py        # Script for training/updating the ML model
├── static/                 # Static assets directory
│   └── style.css          # CSS styling for the web interface
├── templates/             # HTML template directory
│   ├── index.html        # Main page template for email input
│   └── show.html         # Results page template with visual feedback
└── use_model.py          # Utility script for model inference
```

## Usage Instructions
### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

Required Python packages:
```bash
Flask
scikit-learn
python-docx
joblib
```

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd email-spam-detector
```

2. Create and activate a virtual environment:
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask scikit-learn python-docx joblib
```

### Quick Start

1. Start the Flask application:
```bash
python main.py
```

2. Open a web browser and navigate to:
```
http://localhost:5000
```

3. Use the application by either:
   - Pasting email content directly into the text area
   - Uploading an email file (.txt, .eml, .doc, or .docx)

### More Detailed Examples

1. Analyzing a text email:
```python
# Using the model directly
from use_model import loaded_model

email_text = "Get rich quick! Buy now!"
prediction = loaded_model.predict([email_text])
print("Spam" if prediction[0] == 1 else "Ham")
```

2. Retraining the model with new data:
```python
# Using retrain_model.py
from retrain_model import model
X_new = ["New spam example", "New ham example"]
y_new = [1, 0]
model.fit(X_new, y_new)
```

### Troubleshooting

Common Issues:

1. Model File Not Found
```
Error: No such file or directory: 'model.pkl'
Solution: Ensure model.pkl exists in the root directory. Run retrain_model.py to generate it.
```

2. File Upload Issues
```
Error: "Invalid file format"
Solution: Check if the file extension is .txt, .eml, .doc, or .docx
```

3. Memory Issues
```
Error: "MemoryError"
Solution: Reduce the file size to under 16MB or adjust MAX_CONTENT_LENGTH in main.py
```

## Data Flow
The application processes email content through a machine learning pipeline that converts text into numerical features and classifies it using a Naive Bayes model.

```ascii
[User Input] -> [Text Processing] -> [ML Model] -> [Classification]
     ↓              ↓                   ↓              ↓
   Email       Text Cleaning      Feature Vector    Spam/Ham
    File       Normalization      Transformation    Decision
```

Component Interactions:
1. User submits email content through web interface
2. Flask routes the request to the appropriate handler
3. Text processing converts input to model-compatible format
4. Model performs classification using pre-trained weights
5. Results are rendered with visual feedback
6. Optional export to Word document for reporting
7. All file operations use secure temporary storage