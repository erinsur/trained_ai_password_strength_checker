import os
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


try:
    data = joblib.load(os.path.join('data', 'split_data.joblib'))
    X_train = data['X_train']
    X_test = data['X_test']
    y_train = data['y_train']
    y_test = data['y_test']
    print("data finished loading")
except FileNotFoundError:
    print("Could not find 'split_data.joblib' file.")
    exit()

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("data finished scaling")

model = RandomForestClassifier(random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)
print("model has been trained! Now predicting for X_test...")

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
array = confusion_matrix(y_test, y_pred)

print(f"\n--- Model Results ---")
print(f"Random Forest Classifier Accuracy: {accuracy * 100:.2f}%")
print(f"The model correctly predicted strength for {accuracy * len(y_test):.0f} out of {len(y_test)} passwords.")
print(array)
print("True Neg (truly weak), False Pos(it mistaken it for strong)")
print("False Neg(it mistaken it for weak), True Pos(truly strong)")

os.makedirs('models', exist_ok=True) 
joblib.dump(model, os.path.join('models', 'password_classifier_v1.joblib'))
joblib.dump(scaler, os.path.join('models', 'fitted_scaler.joblib'))

print("\n✅ Model and Scaler successfully saved and ready for deployment!")

# This code was used to create the split_data.joblib file (so we dont have to run over and over)
'''
from sklearn.model_selection import train_test_split
import pandas as pd

print("im here")
df = pd.read_pickle(os.path.join('data','processed_data.pkl'))

X = df['features'].tolist()
y = df['strength'].tolist()
print("be patient")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


data_to_save = {
    'X_train': X_train,
    'X_test': X_test,
    'y_train': y_train,
    'y_test': y_test
}

joblib.dump(data_to_save, 'data/split_data.joblib') 
print("finally done)

'''