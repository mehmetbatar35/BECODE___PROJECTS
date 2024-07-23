import shap
shap.initjs()
import pandas as pd
import numpy as np

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

def model_func():

    df = pd.read_csv('01.IMMOELIZA/03.Machine_Learning/shap.csv')
    print(df.head())

    X = df.drop('price', axis=1)
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=50, max_depth=10, n_jobs=-1)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    # print(classification_report(y_pred, y_test))

    explainer = shap.Explainer(clf)
    shap_values = explainer.shap_values(X_test)
    shap.summary_plot(shap_values, X_test)


model_func()

