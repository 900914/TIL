
import lightgbm as lgb
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def main():
    # import iris data
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # split train and test
    X_train, X_test , y_train, y_test = train_test_split(X,y,random_state=42)

    # split evaluation and validation
    X_eval, X_valid, y_eval, y_valid = train_test_split(X_test,y_test, random_state=42)

    # create dataset for lightGBM
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

    params = {
        'objective' : 'multiclass',
        'num_class' : 3,
    }

    # training
    model = lgb.train(
        params=params, 
        train_set=lgb_train, 
        valid_sets=lgb_eval,
        num_boost_round=100,
        early_stopping_rounds=10
        )

    # evaluation
    y_pred_proba = model.predict(X_valid, num_iteration=model.best_iteration)
    y_pred = np.argmax(y_pred_proba, axis=1) # 返り値は確率になっているので最尤に寄せる

    # accuracy 
    accuracy = accuracy_score(y_valid, y_pred)
    print(accuracy)

if __name__ == '__main__':
    main()



    

