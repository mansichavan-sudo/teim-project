import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    'customer_id': range(1, 51),
    'age': [25, 30, 22, 28, 35, 40, 32, 29, 31, 27] * 5,
    'income': [40000, 50000, 45000, 60000, 55000, 52000, 48000, 47000, 51000, 53000] * 5,
    'gender': ['Male', 'Female'] * 25,
    'existing_product': ['Savings', 'Loan', 'Insurance', 'Credit Card', 'Savings'] * 10,
    'target_product': ['Insurance', 'Credit Card', 'Loan', 'Savings', 'Insurance'] * 10
}

df = pd.DataFrame(data)

label_encoders = {}
for column in ['gender', 'existing_product', 'target_product']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

X = df[['age', 'income', 'gender', 'existing_product']]
y = df['target_product']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open('cross_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Cross-sell model trained and saved as cross_model.pkl")
