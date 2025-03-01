import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset (using a dummy dataset for example)
data = {
    'bedrooms': [1, 2, 3, 4, 5],
    'bathrooms': [1, 1, 2, 2, 3],
    'sqft': [500, 800, 1200, 1500, 2000],
    'location': [1, 2, 3, 4, 5],  # Encoding location
    'price': [100000, 150000, 200000, 250000, 300000]
}
df = pd.DataFrame(data)

# Features & target
X = df[['bedrooms', 'bathrooms', 'sqft', 'location']]
y = df['price']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'ml_model/model.pkl')
print("Model trained and saved successfully.")
