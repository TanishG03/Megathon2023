import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load your CSV file into a pandas DataFrame
data = pd.read_csv('personality_data.csv')

# Separate features (X) and labels (y)
X = data.iloc[:, :-5]  # Features (float values)
y = data.iloc[:, -5:]   # Labels (string values)

# Convert string labels to numerical values using LabelEncoder
label_encoders = []
for column in y.columns:
    le = LabelEncoder()
    y[column] = le.fit_transform(y[column])
    label_encoders.append(le)

# Create a decision tree classifier
classifier = DecisionTreeClassifier()

# Train the classifier
classifier.fit(X, y)

# Save the trained model to a file
joblib.dump((classifier, label_encoders), 'ML_ocean_1.pkl')
