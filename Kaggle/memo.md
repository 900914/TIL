
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
- `LightGBM.train()`に`early_stopping_rounds`パラメータを渡すことによって、最適なブーストラウンド数を最適化する。`10`を指定すれば、10ラウンド進めても性能に改善が見られない場合はそこでストップさせる。あまり小さい数値だと、局所最適となってしまう。この機能を使う場合は、学習用データとは別に、`valid_sets`オプションで評価用データを渡す必要がある。
- `lightgbm.train()`の引数
    - `params` 各種パラメータ
    - `lgb_train` トレーニングデータとテストデータ（評価用）データの説明変数が格納されている、`lgb.dataset`を指定
    - `valid_sets` は、説明変数と目的変数セットを1つにして指定。具体的には、`valid_set=(lgb_train, lgb_test)`にて指定。※ `lgb_test`だけで良いのか調査
    - `num_boost_round`は、`=10000`なら、学習を100000回繰り返すということ。
    - `early_stopping_round`は、過学習を防ぐためのもの。`=100`とすれば、100回くらい学習して、過学習しているようならベストなサイクルで学習を終了させる。`num_boost_round`で大きな数値だとしても、学習が止まる。
    - `varbose_eval`は、`=50`なら、学習過程を50サイクルずつ表示
## caegory_encoders


## OPTUNA
- ハイパーパラメータの最適化パッケージ
- ベイズ最適化
- TPEを用いている
- `optuna.create_study()`で`optuna.study`インスタンスを作り、最小化したいスコアを返り値とする関数を定義する。そして、`study`インスタンスの`optimize()`に関数を渡して最適化

## Titanic

### 参考 Kernel
https://www.kaggle.com/weidoudou/a-data-science-framework-to-achieve-99-accuracy  

データサイエンスのフレームワーク
1. Define the Problem
タイタニック号の沈没時の生存結果を予測するアルゴリズムの開発
1. Gather the Data
KaggleにあるTrain/Testデータを利用
1. Prepare Data for Consumption
    1. Correcting：異常値と外れ値の対策  
    今回はとくになし
    1. Completing：欠損値の補完
    年齢を中央地、出港地を最頻値、運賃を中央値で補完など
    1. Creating：特徴量の生成  
    ファミリーサイズの生成など
    1. Converting：機械学習の入力値のために数値化  
    ダミー変数化、連続値の離散化など
1. Perform Exploratory Analysis  
ビジュアライゼーションして、データを調べる。変数の説明・要約をする。また、説明変数と目的変数の相関関係を調べる。
1. Model Data  
データサイエンスは、数学・コンピュータサイエンス・ビジネスマネジメントの学際的な領域である。どれが欠けても良いことはない。Kernelを通じて学ぶべきことは、何をしているかよりも、なぜするのかである。  
- 目的・テーマ設計：ビジネス力が重要
- 問題提議：データサイエンス力が重要
- アプローチの設計：データサイエンス力（数学含む）が重要
- 処理・分析：データエンジニア力（数学含む）が重要
- 解決実行：ビジネス力が重要
1. Validate and Implement Data Model
生存率が80％程度になったら、次はROIを考えたほうがいい。数ヶ月で予測精度が0.1％向上したとしても、ビジネスへのインパクトは微々たるもの。モデル改良はROI（学習時間を費用換算してもいい）をよく考えて取り掛かるべき。QCDの観点ともいえる。Qualityは最優先だが、CostとDeliveryも視野に入れるべき。  
タイタニック問題は、Survived＝０（つまり死亡）が1,502/2,224であることが事実として存在する。したがって、全て０予測したとしても、精度は67.5%である。ベースラインとなる精度（Baseline Accuracy)は、この68%である。
1. Optimize and Strategize

- data1 = data_raw.copy(deep = True) なぜディープコピーするのか
- data_raw.sample(10) 利用
- dataset['FareBin'] = pd.qcut(dataset['Fare'], 4)
- dataset['AgeBin'] = pd.cut(dataset['Age'].astype(int), 5)
- `lgb.__version__` でversion確認

### もう一度、読みます

- https://speakerdeck.com/takapy/xue-xi-tui-lun-paipurainwogou-zhu-surushang-deda-qie-nisiteirukoto
- http://rin-effort.com/2020/01/14/machine-learning-9/
