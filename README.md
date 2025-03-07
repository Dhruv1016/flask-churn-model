🛠 Churn Prediction API**
A Flask-based API for predicting customer churn using XGBoost, featuring SHAP explainability.**

---

📌 Project Overview**
This project builds a customer churn prediction model using `XGBoost`, deployed via Flask API:
- Predicts **customer churn probability**.
- Returns **top 3 influencing factors** using **SHAP explainability**.
- Is deployable via Ngrok or cloud services.
- Can be integrated into **business retention strategies**.

---

📦 Features**
✅ Predicts if a customer will churn**  
✅ Returns churn probability  
✅ Provides top 3 influencing features using SHAP 
✅ Deployed using Flask & Ngrok 
✅ Can be integrated into business applications

---

📂 Project Structure**
```
flask_churn_model/
│── app.py                     # Flask API for churn prediction
│── final_xgb_model.pkl         # Trained XGBoost model
│── feature_columns.pkl         # Feature names for input processing
│── customer_churn_dataset.csv  # Sample dataset (if applicable)
│── requirements.txt            # Python dependencies
│── README.md                   # Documentation
│── .gitignore                  # Files to ignore
```

---

⚙️ Setup & Installation**
1️⃣ Clone the Repository**
```sh
git clone https://github.com/Dhruv1016/flask-churn-model.git
cd flask-churn-model
```

2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed. Then, install required packages:
```sh
pip install -r requirements.txt
```

3️⃣ Run the Flask API
Start the Flask server:
```sh
python app.py
```
By default, it runs on `http://127.0.0.1:5000/`

---

📡 API Usage
1️⃣ Predict Churn
🔹 Endpoint**
```
POST /predict
```
🔹 Request JSON
```json
{
  "Gender": "Male",
  "Total Spend": 500,
  "Tenure": 10,
  "Subscription Type": "Standard",
  "Contract Length": "Monthly"
}
```
🔹 Response JSON
```json
{
  "churn_prediction": 1,
  "churn_probability": 0.78,
  "top_3_features": {
    "Tenure": -0.23,
    "Total Spend": 0.18,
    "Subscription Type_Standard": 0.15
  }
}
```
- `churn_prediction`: `1` (Customer will churn), `0` (Customer will stay)
- `churn_probability`: Likelihood of churn
- `top_3_features`: Key factors driving the decision (SHAP values)

---

🚀 Deployment
1️⃣ Using Ngrok (for local testing)
Run Flask first:
```sh
python app.py
```
Then, in a new terminal, expose it via Ngrok:
```sh
ngrok http 5000
```
Copy the generated URL (e.g., `https://xyz.ngrok-free.app`) and use it for API calls.

2️⃣ Deploy to Cloud (AWS, GCP, Render)
- *AWS EC2: Deploy via Flask and set up `gunicorn`
- Render: Use their free Flask deployment
- Google Cloud Run: Serverless deployment

---

📜 Requirements
Ensure these dependencies are installed (`requirements.txt`):
```
Flask
flask_cors
pandas
numpy
scikit-learn
xgboost
shap
joblib
```

---

🎯 Author
Dhruv Gandhi 
🔗 [GitHub](https://github.com/Dhruv1016) | 📧 *dhruvg3@uw.edu*
