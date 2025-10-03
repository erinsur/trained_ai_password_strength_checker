import os 
import pandas as pd
from feature_engineering import extract_features
import joblib
from sklearn.model_selection import train_test_split

# strong password data
strong_full_file_path = os.path.join('data', 'strong_passwords.txt')
df_strong = pd.read_csv(strong_full_file_path, header=None, names=['password'], on_bad_lines='skip')
df_strong['strength'] = 1 

# weak password data
weak_full_file_path = os.path.join('data', 'weak_passwords.txt')
df_weak = pd.read_csv(weak_full_file_path, header=None, names=['password'], on_bad_lines='skip', encoding='latin-1')
df_weak['strength'] = 0

combined_df = pd.concat([df_strong, df_weak], ignore_index=True)
df = combined_df.sample(frac=1).reset_index(drop=True)

df['features'] = df['password'].apply(extract_features)

X = df['features'].tolist()
y = df['strength'].tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


data_to_save = {
    'X_train': X_train,
    'X_test': X_test,
    'y_train': y_train,
    'y_test': y_test
}

joblib.dump(data_to_save, 'data/split_data.joblib') 
print("finally done")