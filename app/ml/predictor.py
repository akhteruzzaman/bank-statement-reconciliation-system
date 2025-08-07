# ml/predictor.py

import joblib
import numpy as np
from pandas import to_datetime

# Load saved sklearn model and preprocessing objects
model = joblib.load('ml/model.pkl')
scaler = joblib.load('ml/scaler.pkl')
le_description = joblib.load('ml/le_description.pkl')
le_status = joblib.load('ml/le_status.pkl')

def predict_status(amount, date_str, description):
    # Convert date string to UNIX timestamp
    transaction_timestamp = int(to_datetime(date_str).timestamp())

    # Encode description, assign -1 if unknown
    try:
        desc_encoded = le_description.transform([description])[0]
    except ValueError:
        desc_encoded = -1

    # Create feature array
    X = np.array([[amount, transaction_timestamp, desc_encoded]])
    X_scaled = scaler.transform(X)

    # Predict encoded label
    pred_encoded = model.predict(X_scaled)[0]
    # Decode to original label (0 or 1)
    pred_label = le_status.inverse_transform([pred_encoded])[0]

    # Return 1 if matched, else 0
    if str(pred_label).lower() in ['1', 'matched', 'true', 'yes']:
        return 1
    else:
        return 0
