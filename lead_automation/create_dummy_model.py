import pickle

# Path to your pickle file
MODEL_PATH = "upsell_model.pkl"

# Dummy model (can be a dictionary, list, or anything)
dummy_model = {"message": "This is a dummy upsell model"}

# Save it
with open(MODEL_PATH, "wb") as f:
    pickle.dump(dummy_model, f)

print("Dummy upsell_model.pkl created successfully!")
