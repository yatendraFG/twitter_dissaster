import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data (only needed once)
nltk.download('stopwords')
nltk.download('wordnet')

# Load model and vectorizer
with open('nb_classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    text_tokens = text.split()
    filtered_words = [word for word in text_tokens if word not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    return " ".join(lemmatized_words)

# Streamlit UI
st.set_page_config(page_title="Disaster Tweet Classifier", layout="centered")
st.title("🌪️ Disaster Tweet Classifier")
st.write("Enter a tweet below to check whether it's about a real disaster or not.")

tweet = st.text_area("✍️ Your Tweet", height=150)

if st.button("🔍 Predict"):
    if tweet.strip() == "":
        st.warning("Please enter a tweet.")
    else:
        cleaned = clean_text(tweet)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]
        label = "🚨 Disaster Tweet" if prediction == 1 else "✅ Not a Disaster Tweet"
        st.subheader("Prediction:")
        st.success(label)