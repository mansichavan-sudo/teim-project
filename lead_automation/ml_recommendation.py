import os
import pickle

# ===========================
# Load ML Models Safely
# ===========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPS_MODEL_PATH = os.path.join(BASE_DIR, "upsell_model.pkl")
CROSS_MODEL_PATH = os.path.join(BASE_DIR, "cross_model.pkl")

# Upsell Model
if os.path.exists(UPS_MODEL_PATH) and os.path.getsize(UPS_MODEL_PATH) > 0:
    with open(UPS_MODEL_PATH, "rb") as f:
        upsell_model = pickle.load(f)
    print("Upsell model loaded successfully!")
else:
    upsell_model = None
    print("Upsell model missing or empty. Using dummy model.")

# Cross-Sell Model
if os.path.exists(CROSS_MODEL_PATH) and os.path.getsize(CROSS_MODEL_PATH) > 0:
    with open(CROSS_MODEL_PATH, "rb") as f:
        cross_model = pickle.load(f)
    print("Cross-sell model loaded successfully!")
else:
    cross_model = None
    print("Cross-sell model missing or empty. Using dummy model.")

# ===========================
# Prediction Function
# ===========================
def predict_recommendation(features):
    """
    features: list of [lead_type, service_type] as integers
    Returns a dictionary with upsell and cross-sell items
    """
    if upsell_model and cross_model:
        upsell_item = upsell_model.predict([features])[0]
        cross_sell_item = cross_model.predict([features])[0]
        return {"upsell": upsell_item, "cross_sell": cross_sell_item}
    else:
        # Dummy recommendations if models are not loaded
        return {"upsell": "N/A", "cross_sell": "N/A"}
