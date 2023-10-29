import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Read data from CSV file into a pandas DataFrame
data = pd.read_csv('dataset.csv')

# Extract features (5 integers) and labels (strings) from the DataFrame
features = data[['c','n','a','e','o']]
labels = data['job']

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.1, random_state=42)

model = RandomForestClassifier()

model.fit(X_train, y_train)

with open('ML_ocean.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
