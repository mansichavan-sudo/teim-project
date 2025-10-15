# ml_model.py (example for upsell)
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("lead_recommendation_dataset.csv")

# Encode categorical variables
le_lead = LabelEncoder()
df['lead_type_enc'] = le_lead.fit_transform(df['lead_type'])

le_service = LabelEncoder()
df['service_type_enc'] = le_service.fit_transform(df['service_type'])

le_upsell = LabelEncoder()
df['upsell_enc'] = le_upsell.fit_transform(df['upsell_item'])

X = df[['lead_type_enc','service_type_enc','past_interactions']]
y = df['upsell_enc']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model & encoders
with open("upsell_model.pkl", "wb") as f:
    pickle.dump((model, le_upsell, le_lead, le_service), f)
