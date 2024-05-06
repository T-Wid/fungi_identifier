import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def main(gc, pop, spc, bs, sr):
    df = pd.read_csv('static/fungi.csv')

    kc = df[['class', 'gill-color', 'population', 'spore-print-color', 'stalk-root', 'bruises']]

    LE = LabelEncoder()
    for column in kc.columns:
        kc[column] = LE.fit_transform(kc[column])

    keys = kc.loc[
        (kc['gill-color'] == gc) &
        (kc['population'] == pop) &
        (kc['spore-print-color'] == spc) &
        (kc['bruises'] == bs) &
        (kc['stalk-root'] == sr)
        ]
    return keys


def classify(userSelection):
    df = pd.read_csv('static/fungi.csv')

    kc = df[['class', 'gill-color', 'population', 'spore-print-color', 'stalk-root', 'bruises']]

    LE = LabelEncoder()
    for column in kc.columns:
        kc[column] = LE.fit_transform(kc[column])

    try:

        X = userSelection.drop(['class'], axis=1)
        Y = userSelection["class"]

        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, random_state=42, test_size=.3, train_size=.7)
        rf = RandomForestClassifier(n_estimators=100,
                                    random_state=50)
        rf.fit(X_train, Y_train)

        accuracy = round(rf.score(X_test, Y_test) * 100, 2)
        preds = list(rf.predict(X_test))
        if preds[0] == 1:
            predictedClass = 'toxic! '
        else:
            predictedClass = 'non-toxic! '
        predictions = int(len(preds))
        message = "Predicted class: {}".format(predictedClass) + "Prediction accuracy was {}%".format(
            accuracy) + " correct for {}".format(predictions) + " specimens."
        if predictions > 0:
            return message
        else:
            return 'Not Enough Data'
    except ValueError:
        return 'This combination did not provide enough information to classify. Try another combination of attributes.'