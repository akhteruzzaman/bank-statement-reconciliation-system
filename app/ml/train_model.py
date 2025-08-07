import os
import django
import sys
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Add the project root to sys.path
sys.path.append('/app')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsrsproject.settings')

# Setup Django
django.setup()

from reconciliation.models import BankTransaction

# ✅ Load all transaction data
queryset = BankTransaction.objects.all().values()
df = pd.DataFrame.from_records(queryset)

# ✅ Drop rows with missing required fields
df.dropna(subset=['amount', 'date', 'description', 'status'], inplace=True)

# ✅ Convert datetime to numeric (timestamp)
df['transaction_timestamp'] = pd.to_datetime(df['date']).astype(np.int64) // 10**9  # UNIX timestamp

# ✅ Encode categorical text fields
le_description = LabelEncoder()
df['description_encoded'] = le_description.fit_transform(df['description'])

le_status = LabelEncoder()
df['status_encoded'] = le_status.fit_transform(df['status'])

# ✅ Define features and labels
X = df[['amount', 'transaction_timestamp', 'description_encoded']]
y = df['status_encoded']

# ✅ Normalize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# ✅ Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model (RandomForest for example)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Save model and scaler
joblib.dump(model, '/app/ml/model.pkl')
joblib.dump(scaler, '/app/ml/scaler.pkl')
joblib.dump(le_description, '/app/ml/le_description.pkl')
joblib.dump(le_status, '/app/ml/le_status.pkl')

print("✅ Model training completed and saved successfully.")
