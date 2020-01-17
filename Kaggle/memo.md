
- Kaggle API データダウンロードの方法。  
`-p ./`　でカレントディレクトリにデータ保存
```python
kaggle competitions download -c home-credit-default-risk -p ./
```
## LightGBMとはなにか？
- ライトビージーエム
- 決定木アルゴリズムに基づく
- 決定木アルゴリズム（モデル）は、ジニ係数（もしくはエントロピー）を利用して分類していく（ジニ係数が高い場合は混在している＝うまく分類されてない）
- LightGBM以外に決定木モデルには、XGBoost、RandomForest等がある
- 勾配ブースティングである(Gradient Boosting)。XGBoostもブースティング手法を採用している
- RandomForestはバギング手法を採用している
- バイアス（偏り）とバリアンス（分散）のうち、ブースティングはバイアスをへらす動きをする（未学習を減らす）lilli
- バイアス（偏り）とバリアンス（分散）のうち、バギングはバリアンスを減らす動きをする（過学習を減らす）
- 勾配ブースティングはアンサンブル学習のブースティング手法を使う
- アンサンブル学習（Ensemble Learning）は複数のモデル（学習器）を融合させて１つの学習モデルを生成する手法
- アンサンブル学習は3つの手法に分けられる。バギング、ブースティング、スタッキング。
- バギングはそれぞれのモデルを並列的に学習を行う
- ブースティングは前の弱学習器(weak leaner)の結果を次の学習データに反映させる
- 決定木を弱学習器としてバギングによるアンサンブル学習の手法をランダムフォレストと呼ぶ
- 勾配ブースティングは、決定木はを弱学習器としてブースティングの手法を用いてアンサンブル学習する
- 勾配ブースティングは、複数の弱学習器（LightGBMの場合は決定木）を１つにまとめるアンサンブル学習のブースティングを用いた手法
- 勾配ブースティングは、それぞれの弱学習器の誤差を学習することが最大特徴
- 計算値をヒストグラムとして扱うのでメモリを抑えられる
- 基本的にはランダムフォレストを先に試したほうがいい（らしい）
- 並列化できない（前回の結果を利用するため）ので訓練にかかる時間は短縮できない
- パラメータに影響されやすいので、チューニングは慎重に
- 主なパラメータは、`n_estimators`と`learning_rate`である
- `max_depth`は、5以下に設定される場合が多い
- ハイパーパラメータは、ツリー固有のパラメータ、ブースティングパラメータ、その他パラメータの大きく３つがある
- `category_encoders`でカテゴリエンコーディングした場合は、`lgb.Dataset`時に`categorical_feature`を指定しないで良い。（エラーが出る）
- `Plotting`
    - `lightgbm.plot_importance`
    - `lightgbm.plot_split_value_histogram`

## caegory_encoders


## OPTUNA
- ハイパーパラメータの最適化パッケージ
- ベイズ最適化
- TPEを用いている
- `optuna.create_study()`で`optuna.study`インスタンスを作り、最小化したいスコアを返り値とする関数を定義する。そして、`study`インスタンスの`optimize()`に関数を渡して最適化

## Titanic

### 参考 Kernel
https://www.kaggle.com/weidoudou/a-data-science-framework-to-achieve-99-accuracy  

- data1 = data_raw.copy(deep = True) なぜディープコピーするのか
- data_raw.sample(10) 利用
- dataset['FareBin'] = pd.qcut(dataset['Fare'], 4)
- dataset['AgeBin'] = pd.cut(dataset['Age'].astype(int), 5)
- `lgb.__version__` でversion確認

