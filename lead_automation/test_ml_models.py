import os
import pickle

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPS_MODEL_PATH = os.path.join(BASE_DIR, "upsell_model.pkl")
CROSS_MODEL_PATH = os.path.join(BASE_DIR, "cross_model.pkl")

# ----------------------------
# Load Models
# ----------------------------
if os.path.exists(UPS_MODEL_PATH) and os.path.getsize(UPS_MODEL_PATH) > 0:
    with open(UPS_MODEL_PATH, "rb") as f:
        upsell_model, le_upsell, le_lead, le_service = pickle.load(f)
    print("Upsell model loaded successfully!")
else:
    upsell_model = le_upsell = le_lead = le_service = None
    print("Upsell model not found!")

if os.path.exists(CROSS_MODEL_PATH) and os.path.getsize(CROSS_MODEL_PATH) > 0:
    with open(CROSS_MODEL_PATH, "rb") as f:
        cross_model, le_cross, _, _ = pickle.load(f)
    print("Cross-sell model loaded successfully!")
else:
    cross_model = le_cross = None
    print("Cross-sell model not found!")

# ----------------------------
# Test Prediction
# ----------------------------
def safe_transform(label, label_encoder):
    """Transform label safely; fallback if unseen."""
    if label_encoder is None:
        return 0  # default encoding
    if label not in label_encoder.classes_:
        print(f"Unseen label '{label}', using fallback.")
        label = label_encoder.classes_[0]
    return label_encoder.transform([label])[0]

# Example inputs
test_lead_type = "Hot"       # try changing to "Unknown" to test fallback
test_service_type = "Product" # try changing to "UnknownService" to test fallback
past_interactions = 2

try:
    if upsell_model and cross_model:
        lead_enc = safe_transform(test_lead_type, le_lead)
        service_enc = safe_transform(test_service_type, le_service)
        X_test = [[lead_enc, service_enc, past_interactions]]

        ups_pred = le_upsell.inverse_transform(upsell_model.predict(X_test))[0]
        cross_pred = le_cross.inverse_transform(cross_model.predict(X_test))[0]

        print("Upsell Recommendation:", ups_pred)
        print("Cross-sell Recommendation:", cross_pred)
    else:
        print("Models not loaded. Cannot predict.")
except Exception as e:
    print("Prediction Error:", e)
