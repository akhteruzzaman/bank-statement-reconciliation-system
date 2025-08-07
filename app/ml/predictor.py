import joblib
import numpy as np
import pandas as pd


# Load saved model and preprocessing tools
model = joblib.load('ml/model.pkl')
scaler = joblib.load('ml/scaler.pkl')
le_description = joblib.load('ml/le_description.pkl')
le_company = joblib.load('ml/le_company.pkl')
le_reference = joblib.load('ml/le_reference.pkl')
le_invoice = joblib.load('ml/le_invoice.pkl')
le_status = joblib.load('ml/le_status.pkl')

def predict_status(company, description, amount, reference_number, invoice_no, date_str):
    # Convert date to timestamp
    transaction_timestamp = int(pd.to_datetime(date_str).timestamp())

    # Handle unknown values using safe encoding
    def safe_encode(label_encoder, value):
        try:
            return label_encoder.transform([value])[0]
        except ValueError:
            return -1

    company_encoded = safe_encode(le_company, company)
    desc_encoded = safe_encode(le_description, description)
    ref_encoded = safe_encode(le_reference, reference_number)
    invoice_encoded = safe_encode(le_invoice, invoice_no)

    # Create feature array
    X = np.array([[company_encoded, desc_encoded, amount, ref_encoded, invoice_encoded]])
    X_scaled = scaler.transform(X)

    # Predict
    pred_encoded = model.predict(X_scaled)[0]
    pred_label = le_status.inverse_transform([pred_encoded])[0]

    return 1 if str(pred_label).lower() in ['1', 'matched', 'true', 'yes'] else 0
