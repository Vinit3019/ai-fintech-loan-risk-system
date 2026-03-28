import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Create dummy dataset
data = {
    "income": np.random.randint(20000, 100000, 200),
    "credit_score": np.random.randint(300, 850, 200),
    "loan_amount": np.random.randint(50000, 500000, 200),
}

df = pd.DataFrame(data)

# Target: simple rule
df["approved"] = ((df["credit_score"] > 600) & (df["income"] > 40000)).astype(int)

X = df[["income", "credit_score", "loan_amount"]]
y = df["approved"]

model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")