import lightgbm as lgb
from sklearn import datasets
from sklearn.model_selection import train_test_split
import  matplotlib.pyplot as plt


def main():
    # import iris data
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # split train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # create datasets for lightgbm
    lgb_train = lgb.Dataset(X_train, y_train, feature_name=iris.feature_names)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

    # parameters
    params = {
        'objective':'multiclass',
        'num_class':3,
    }

    # training
    model = lgb.train(
        params=params, 
        train_set=lgb_train, 
        valid_sets=lgb_eval, 
        num_boost_round=40
        )

    lgb.plot_importance(model, figsize=(12,6))
    plt.show()

if __name__ == '__main__':
    main()


