
# lightGBM_basic.py の sklearn用

import lightgbm as lgb
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

def main():
    # import Iris data

    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # Split train data and test data
    X_train, X_test, y_train, y_test = train_test_split(X,y)

    # training
    model = lgb.LGBMClassifier()
    model.fit(X_train, y_train)

    # predict
    y_pred = model.predict_proba(X_test)
    y_pred_max = np.argmax(y_pred, axis=1)

    # accuracy
    accuracy = sum(y_test == y_pred_max)/len(y_test)
    print(accuracy)


if __name__ == '__main__':
    main()




