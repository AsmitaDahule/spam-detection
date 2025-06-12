# Spam Detection Web App 

A simple web application that detects whether a given message is **Spam** or **Not Spam** using Machine Learning and Flask.

##  Features

- Enter any text message
- Machine Learning-based classification
- Beautiful and responsive UI (HTML + CSS)
- Built with Flask backend
- Trained with Naive Bayes & TF-IDF

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn (Naive Bayes, TfidfVectorizer)
- **Data**: SMS Spam Collection Dataset

---

##  Project Structure

spam-detection-app/
│
├── app.py # Main Flask backend
├── train_model.py # ML training script
├── spam_model.pkl # Trained ML model
├── vectorizer.pkl # Saved TF-IDF vectorizer
│
├── templates/
│ └── index.html # Frontend UI template
│
├── static/
│ └── style.css # UI Styling
│
└── README.md # Project overview


---

##  How It Works

1. **Train the Model**
   - `train_model.py` loads the dataset and trains a Naive Bayes classifier.
   - It saves the trained model and vectorizer as `.pkl` files.

2. **Run the App**
   - `app.py` starts a Flask server.
   - The form in the frontend sends the input to the backend.
   - Backend predicts and returns whether it is **Spam** or **Not Spam**.

---

##  Getting Started

###  Clone this Repository
```bash
git clone https://github.com/yourusername/spam-detection-app.git
cd spam-detection-app




 Install Dependencies
    pip install flask scikit-learn pandas

 Train the Model
    python train_model.py

 Run the App
    python app.py
    Visit http://127.0.0.1:5000 in your browser.

dataset used : https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset


 Made by
    Asmita Dahule
    Passionate about Web Dev + Machine Learning