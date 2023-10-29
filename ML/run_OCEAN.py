import joblib
import pandas as pd

# Load the machine learning model from the file
def load_model(model_file_path):
    return joblib.load(model_file_path)

# Get user input for 5 features
def get_user_input():
    feature_names = ['c','n','a','e','o']
    feature_values = []
    for name in feature_names:
        value = float(input(f"Enter {name}: "))
        feature_values.append(value)
    # Return a pandas DataFrame with named columns
    feature_values[2]=5-feature_values[2]
    return pd.DataFrame([feature_values], columns=feature_names)

# Main function
def main():
    model_file_path = 'ML_ocean.pkl'  # Replace with the actual file path of your model
    model = load_model(model_file_path)

    # Get user input for features
    input_features = get_user_input()

    # Make prediction using the loaded model
    predicted_label = model.predict(input_features)
    print("Predicted Label:", predicted_label[0])

if __name__ == "__main__":
    main()
