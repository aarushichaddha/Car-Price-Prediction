import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("dataset/car data.csv")

# Remove unnecessary column
df.drop("Car_Name", axis=1, inplace=True)

# Convert Year into Car Age
current_year = 2025
df["Car_Age"] = current_year - df["Year"]
df.drop("Year", axis=1, inplace=True)

# One Hot Encoding
df = pd.get_dummies(df, drop_first=True)

# Split data
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# Save column names
pickle.dump(X.columns.tolist(), open("columns.pkl", "wb"))

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestRegressor(
    n_estimators=500,
    random_state=42
)

model.fit(X_train, y_train)

# Save Model
pickle.dump(model, open("prediction_model.pkl", "wb"))

print("Model Saved Successfully!")