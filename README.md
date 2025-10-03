# AI Password Strength Checker
This project implements a complete, containerized Machine Learning pipeline to classify a given password as either STRONG or WEAK. It uses a Random Forest Classifier trained on manually engineered features derived from password complexity.
The entire application is packaged with Docker for guaranteed reproducibility.

## Quick Start (Using Docker)
The fastest and most reliable way to use this predictor is via the containerized image.
### Prerequisites
You must have the Docker intalled and running.

### 1. Build the Image
Run the following command in the project root directory where the Dockerfile is located. This will build the image and tag it password-checker.

```
docker build -t password-checker .
```

### 2. Run the Prediction
Use the docker run command, passing the password in quotes as an argument.

*Example 1: Predict a Weak Password*
```
docker run --rm password-checker "password123"
```

*Example 2: Predict a Strong Password*
```
docker run --rm password-checker "My_Complex!Password#1A"
```

## ⚙️ Project Structure & Development Workflow

This repository is structured to separate the slow data processing tasks from the fast deployment tasks, ensuring an efficient developer experience.

| File/Folder | Purpose | Execution Frequency |
| :--- | :--- | :--- |
| `data_prep.py` | One-time script to load raw data, perform feature engineering, and create `data/split_data.joblib`. | Run Once (on initial setup). |
| `model_training.py` | Loads `split_data.joblib`, trains the Random Forest Classifier, and saves the final model/scaler to `models/`. | Run when training a new model. |
| `predict.py` | The main prediction script. Loads the saved model/scaler and accepts a password argument via CLI. | Run for deployment or testing. |
| `feature_engineering.py` | Defines the `extract_features` function used by both `data_prep.py` and `predict.py`. | Core logic. |
| `Dockerfile` | Instructions to package the `predict.py` and `models/` into a portable image. | Run when building the image. |
| `.dockerignore` | Excludes large data files and training scripts from the final image build. | Build efficiency. |
| `requirements.txt` | Lists pinned Python dependencies to prevent version conflicts (e.g., scikit-learn). | Build reliability. |
| `models/` | Stores the final `password_classifier_v1.joblib` and `fitted_scaler.joblib`. | Output of `model_training.py`. |
