import random
import csv


def analyze_personality(random_value,random_value2,random_value3,random_value4,random_value5):
    
    # Calculate personality scores
    openness_score = random_value
    conscientiousness_score = random_value2
    extraversion_score = random_value3
    agreeableness_score = random_value4
    # Emotional Stability is the opposite of Neuroticism
    emotional_stability_score = random_value5

    # Interpret individual personality traits using descriptive words
    if openness_score > 4:
        openness_interpretation = "Highly Creative and Imaginative"
    elif openness_score > 3:
        openness_interpretation = "Creative and Curious"
    elif openness_score > 2:
        openness_interpretation = "Moderately Open to New Experiences"
    elif openness_score > 1:
        openness_interpretation = "Practical and Down-to-Earth"
    else:
        openness_interpretation = "Conventional and Traditional"
    
    if conscientiousness_score > 4:
        conscientiousness_interpretation = "Highly Disciplined and Organized"
    elif conscientiousness_score > 3:
        conscientiousness_interpretation = "Disciplined and Responsible"
    elif conscientiousness_score > 2:
        conscientiousness_interpretation = "Moderately Conscientious"
    elif conscientiousness_score > 1:
        conscientiousness_interpretation = "Carefree and Spontaneous"
    else:
        conscientiousness_interpretation = "Impulsive and Disorganized"
    
    if extraversion_score > 4:
        extraversion_interpretation = "Very Sociable and Outgoing"
    elif extraversion_score > 3:
        extraversion_interpretation = "Sociable and Energetic"
    elif extraversion_score > 2:
        extraversion_interpretation = "Moderately Extraverted"
    elif extraversion_score > 1:
        extraversion_interpretation = "Reserved and Introverted"
    else:
        extraversion_interpretation = "Very Reserved and Shy"
    
    if agreeableness_score > 4:
        agreeableness_interpretation = "Highly Compassionate and Empathetic"
    elif agreeableness_score > 3:
        agreeableness_interpretation = "Compassionate and Friendly"
    elif agreeableness_score > 2:
        agreeableness_interpretation = "Moderately Agreeable"
    elif agreeableness_score > 1:
        agreeableness_interpretation = "Assertive and Tough-minded"
    else:
        agreeableness_interpretation = "Very Assertive and Competitive"
    
    if emotional_stability_score > 4:
        emotional_stability_interpretation = "Very Emotionally Stable and Calm"
    elif emotional_stability_score > 3:
        emotional_stability_interpretation = "Emotionally Stable and Relaxed"
    elif emotional_stability_score > 2:
        emotional_stability_interpretation = "Moderately Emotionally Stable"
    elif emotional_stability_score > 1:
        emotional_stability_interpretation = "Anxious and Sensitive"
    else:
        emotional_stability_interpretation = "Very Anxious and Reactive"


    return openness_interpretation, conscientiousness_interpretation, extraversion_interpretation, agreeableness_interpretation, emotional_stability_interpretation


def generate_personality_data(num_samples, output_csv_filename):
    with open(output_csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Emotional Stability', 'Trait1', 'Trait2', 'Trait3', 'Trait4', 'Trait5']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_samples):
            random_value = random.uniform(0, 5)
            random_value2 = random.uniform(0, 5)
            random_value3 = random.uniform(0, 5)
            random_value4 = random.uniform(0, 5)
            random_value5 = random.uniform(0, 5)
            openness, conscientiousness, extraversion, agreeableness, emotional_stability = analyze_personality(random_value, random_value2, random_value3, random_value4, random_value5)
            writer.writerow({
                'Openness': random_value,
                'Conscientiousness': random_value2,
                'Extraversion': random_value3,
                'Agreeableness': random_value4,
                'Emotional Stability': random_value5,
                'Trait1': openness,
                'Trait2': conscientiousness,
                'Trait3': extraversion,
                'Trait4': agreeableness,
                'Trait5': emotional_stability
            })

# Generate a CSV file with 100 samples
generate_personality_data(100, 'personality_data.csv')
