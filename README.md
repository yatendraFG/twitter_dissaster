

# 🚨 Tweet Disaster Classification (Flask Web App)

This project is a machine learning-based web application that classifies tweets as **Disaster** or **Not Disaster** using a Multinomial Naive Bayes model trained on a tweet dataset. The app is built using **Flask** for backend and **HTML** for a simple frontend interface.

---

## 📁 Project Structure

├── app.py # Flask web app ├── model.pkl # Trained classification model (MultinomialNB) ├── vectorizer.pkl # Fitted TfidfVectorizer or CountVectorizer ├── templates/ │ └── index.html # Web UI for user input ├── Tweet_disaster_project_7.ipynb # Jupyter Notebook for model training ├── README.md # You're here

yaml
Copy
Edit

---

## ⚙️ Installation

1. Clone the repository or download the files.
2. Install the required Python packages:

```bash
pip install flask pandas numpy scikit-learn joblib
🧠 Model Training
Model training is done in Tweet_disaster_project_7.ipynb. It includes:

Data loading and preprocessing

Vectorization using CountVectorizer or TfidfVectorizer

Classification with MultinomialNB

Saving the model and vectorizer:

python
Copy
Edit
import joblib
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
🚀 Run the App
After training and saving your model/vectorizer:

bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000 in your browser.

📝 How to Use
Enter a tweet in the input field.

Click Classify.

Get a result: either "Disaster" or "Not Disaster".

📌 Notes
Ensure your model.pkl and vectorizer.pkl match the training vocabulary.

Don't re-fit the vectorizer on new input — just use .transform().

📧 Contact
For any questions or collaboration inquiries, feel free to reach out!

8233322296 

Let me know if you'd like this customized with GitHub badges, image previews, or deployment info (like on Heroku or Render).
