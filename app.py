from flask import Flask, request, jsonify
import joblib
import pandas as pd
import shap
import numpy as np 

app = Flask(__name__)

model = joblib.load("final_xgb_model.pkl")
feature_names = joblib.load("feature_columns.pkl")  

explainer = shap.TreeExplainer(model)

def preprocess_input(data):
    df_input = pd.DataFrame([data])
    
    df_input['Gender'] = df_input['Gender'].map({'Male': 0, 'Female': 1})
    df_input['AvgSpendPerMonth'] = df_input['Total Spend'] / df_input['Tenure']
    df_input = pd.get_dummies(df_input, columns=['Subscription Type', 'Contract Length'], drop_first=True)

    for col in feature_names:
        if col not in df_input.columns:
            df_input[col] = 0  

    df_input = df_input[feature_names]  
    return df_input

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    X_new = preprocess_input(input_data)

    churn_prob = model.predict_proba(X_new)[0, 1]
    churn_pred = int(churn_prob >= 0.5)

    shap_values = explainer(X_new).values[0]
    feature_importance = dict(zip(feature_names, shap_values))

    top_3_features = sorted(feature_importance.items(), key=lambda x: abs(x[1]), reverse=True)[:3]

    response = {
        "churn_prediction": churn_pred,
        "churn_probability": round(float(churn_prob), 3),
        "top_3_features": {feature: round(float(value), 3) for feature, value in top_3_features} 
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
