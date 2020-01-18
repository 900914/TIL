import lightgbm as lgb
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt


def main():
    # import datasets
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # create dataset for lgb
    lgb_train = lgb.Dataset(X,y)

    # parameters
    params = {
        'objective':'multiclass',
        'num_class':3,
    }

    # cross validation
    cv_results = lgb.cv(params=params, train_set=lgb_train, nfold=10)
    cv_logloss = cv_results['multi_logloss-mean']
    round_n = np.arange(len(cv_logloss))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(round_n,cv_logloss)
    plt.show()

if __name__ == '__main__':
    main()

