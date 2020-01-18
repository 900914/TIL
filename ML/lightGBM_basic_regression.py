
# 回帰問題
import  lightgbm as lgb 
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

import optuna
from optuna.integration import lightgbm_tuner

def main():

    # load dataset
    boston = datasets.load_boston()
    X , y = boston.data, boston.target

    # split train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # create dataset for lightgbm
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test)

    # parameters
    params = {
        'objective':'regression',
        'metric':'rmse'  # RMSE（Root Mean Square Error ,平均二乗誤差平方根）
    }

    # stepwise tuning of OPTUNA

    best_params = {}
    tuning_history = []

    # training , train_setは説明変数が入ってる。
    model = lightgbm_tuner.train(
                        params=params, 
                        train_set=lgb_train, 
                        valid_sets=(lgb_train,lgb_eval),
                        early_stopping_rounds=100,
                        num_boost_round=10000,
                        verbose_eval=50,
                        best_params=best_params,
                        tuning_history=tuning_history
                        )

    # prediction
    y_pred = model.predict(data=X_test, num_iteration=model.best_iteration)

    # caluculate RMSE
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    print(rmse)
    

    fig  = plt.figure()
    ax = fig.add_subplot(1,1,1)
    lgb.plot_importance(model,height=0.5, ax=ax,figsize=(8,10))
    plt.show()

    print(best_params)
    print(tuning_history)

    
if __name__ == '__main__':
    main()

