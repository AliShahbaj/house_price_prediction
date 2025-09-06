# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Step 1: Create sample dataset (size vs. price)
data = {
    "size": [500, 1000, 1500, 2000, 2500],
    "price": [100000, 200000, 300000, 400000, 500000]
}
df = pd.DataFrame(data)

# Step 2: Train model
X = df[["size"]]   # features
y = df["price"]    # target

model = LinearRegression()
model.fit(X, y)

# Step 3: Test prediction (using DataFrame instead of plain list → fixes warning)
test_data = pd.DataFrame({"size": [1800]})
print(model.predict(test_data))  # Example: predict price of 1800 sq ft

# Step 4: Save model to file
with open("house_price_model.pkl", "wb") as f:
    pickle.dump(model, f)
