from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np

# Define your Pydantic model for incoming data
class EmailText(BaseModel):
    text: str

app = FastAPI()

# Load CountVectorizer and the logistic regression model
cv = load('count_vectorizer.joblib')
clf = load('logistic_regression_model.joblib')

# Define a function to clean text (placeholder, implement according to your requirements)
def clean_text(text):
    # Implement your cleaning here
    cleaned_text = text.lower()  # Simple example, replace with your actual cleaning process
    return cleaned_text

@app.post("/predict/")
async def predict_email(email: EmailText):
    cleaned_email = clean_text(email.text)
    features = cv.transform([cleaned_email]).toarray()
    prediction = clf.predict(features)
    result = "Spam" if prediction[0] == 1 else "Not Spam"
    return {"prediction": result}
