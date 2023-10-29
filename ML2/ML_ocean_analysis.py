import pandas as pd
import joblib

# Load your new data point(s) into a pandas DataFrame
openness = float(input("Enter Openness: "))
conscientiousness = float(input("Enter Conscientiousness: "))
extraversion = float(input("Enter Extraversion: "))
agreeableness = float(input("Enter Agreeableness: "))
emotional_stability = float(input("Enter Emotional Stability: "))

# Create a DataFrame for the user input
new_data = pd.DataFrame({
    'Openness': [openness],
    'Conscientiousness': [conscientiousness],
    'Extraversion': [extraversion],
    'Agreeableness': [agreeableness],
    'Emotional Stability': [emotional_stability]
})

# Load the saved model and label encoders
classifier, label_encoders = joblib.load('ML_ocean_1.pkl')

# Predict numerical values for the new data point(s)
predicted_values = classifier.predict(new_data)

# Convert the predicted numerical values back to string labels
predicted_labels = []
for i, le in enumerate(label_encoders):
    predicted_labels.append(le.inverse_transform(predicted_values[:, i]))

# Print the predicted string values
for label in predicted_labels:
    print(label[0])
