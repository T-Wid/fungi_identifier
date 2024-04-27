import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv('static/mushrooms.csv')

# Key characteristics
kc = df[['class', 'gill-color', 'population', 'spore-color', 'stalk-root', 'bruises']]


# Function to filter data based on user-selected parameters
def main(gill_color, population, spore_color, bruises, stalk_root):
    keys = kc.loc[
        (kc['gill-color'] == gill_color) &
        (kc['population'] == population) &
        (kc['spore-color'] == spore_color) &
        (kc['bruises'] == bruises) &
        (kc['stalk-root'] == stalk_root)
        ]
    return keys


# Transforming categorical data to ordinal
LE = LabelEncoder()
for column in kc.columns:
    kc[column] = LE.fit_transform(kc[column])


# Function to classify mushroom as edible or poisonous
def classify(user_selection):
    try:
        # Separate features and target variable
        X = user_selection.drop(['class'], axis=1)
        Y = user_selection["class"]

        # Split data into train and test sets
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=40, test_size=.5, train_size=.5)

        # Train Random Forest classifier
        rf = RandomForestClassifier(n_estimators=50, random_state=42)
        rf.fit(X_train, Y_train)

        # Calculate accuracy
        accuracy = round(rf.score(X_test, Y_test) * 100, 2)
        predictions = list(rf.predict(X_test))

        # Determine predicted class
        if predictions[0] == 1:
            predicted_class = 'Toxic! Stay away!'
        else:
            predicted_class = 'Non-Toxic! Enjoy!'

        # Prepare result message
        predictions = len(predictions)
        message = f"Predicted class: {predicted_class}. Confidence in predictions is {accuracy}% accurate for {predictions}."

        if predictions > 0:
            return message
        else:
            return 'Not Enough Data to predict.'
    except ValueError:
        return 'No matches were found based on input. Try another combination.'
