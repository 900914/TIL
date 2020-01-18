
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

    # create dataset for lightgbm
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

    # parameter
    params = {
        'objective': 'multiclass',
        'num_class': 3
    }

    # training
    model = lgb.train(params=params, train_set = lgb_train, valid_sets=lgb_eval)

    # predict

    y_pred = model.predict(X_test, num_iteration=model.best_iteration)

    y_pred_max = np.argmax(y_pred , axis=1)

    # accuracy

    accuracy = sum(y_test == y_pred_max) / len(y_test)
    print(accuracy)

if __name__ == '__main__':
    main()

