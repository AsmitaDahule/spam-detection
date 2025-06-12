from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]
    message_transformed = vectorizer.transform([message])
    prediction = model.predict(message_transformed)[0]
    return render_template("index.html", prediction="Spam" if prediction == 1 else "Not Spam", message=message)

if __name__ == "__main__":
    app.run(debug=True)
