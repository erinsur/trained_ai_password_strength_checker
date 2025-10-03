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

Example 1: Predict a Weak Password
```
docker run --rm password-checker "password123"
```

Example 2: Predict a Strong Password
```
docker run --rm password-checker "My_Complex!Password#1A"
```
