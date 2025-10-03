'''

PASSWORD STRENGTH PREDICTOR (CLI)

This script provides the final, deployed prediction tool. It performs the following steps:
1. Uses 'argparse' to accept a password string directly from the command line.
2. Applies the exact same 'extract_features' logic used during training.
3. Loads the saved 'fitted_scaler.joblib' and scales the features.
4. Loads the final trained model ('password_classifier_v1.joblib').
5. Predicts the strength (0=Weak, 1=Strong) and prints a user-friendly message.

'''


import os
import argparse
from feature_engineering import extract_features
import joblib
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("password", help='Enter your password to see strength')
args = parser.parse_args()

arr = extract_features(args.password)
arr = np.array(arr)
arr = arr.reshape(1,-1)

try:
    with open(os.path.join('models', 'fitted_scaler.joblib'), 'rb') as f: 
        scaler = joblib.load(f)
    scaled_arr = scaler.transform(arr)
except FileNotFoundError:
    print("Error: Scaler file not found. Ensure model_training.py was run successfully.")
    exit()

try:
    with open(os.path.join('models', 'password_classifier_v1.joblib'), 'rb') as f:
        model = joblib.load(f)
    strength_score = model.predict(scaled_arr)

    if strength_score == 1:
        print(f"\nPassword is strong!\n")
    else:
        print(f"\nPassword is weak!\n")
except FileNotFoundError:
    print("Error: Model file not found. Ensure model_training.py was run successfully.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
