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


model2=joblib.load('ML_ocean.pkl')
feature_names = ['c','n','a','e','o']
feature_values = [0,0,0,0,0]
feature_values[0]=conscientiousness
feature_values[1]=5-emotional_stability
feature_values[2]=agreeableness
feature_values[3]=extraversion
feature_values[4]=openness
values=pd.DataFrame([feature_values], columns=feature_names)
predicted_label = model2.predict(values)
print("This person is suitable to the roles: ", predicted_label[0])
