
## pandas.DataFrame.interpolate

欠損値NaNを前後の値から補間する  

- 行 or 列を指定: 引数axis(デフォルトは列に対して行われる)
- 補間する連続欠損値の最大数を指定: 引数limit　
- 補間方向を指定: 引数limit_direction
- 内挿のみ or 外挿のみ or 両方を指定: 引数limit_area
- オブジェクト自体を更新するかを指定: 引数inplace
- 保管方法： 引数method(デフォルトはlinier)


### 行を絞り込む
最後の行を抽出しようとして、`df.loc(-1)`とするとエラーになる。この場合は、`df.shape[0]-1`とする。shapeから得られる行・列の行数を取得し、更に`-1`とすることで０から始まる行番号の最後を指定できる。

### apply メソッド

apply関数は、主にデータクリーニングに関わる関数として利用される。`for`ループを持ちいるのに似ているが、その処理を同時に行う点がことなる。そしてapply 関数のほうが高速である。  

Pandasオブジェクト（pandas.DataFrame,pandas.Series)に関数を適用するには、NumPyの関数の引数にPandasオブジェクトを指定する方法と、Pandasオブジェクトのメソッドで関数を適用する方法の２つがある。  

Pandasオブジェクトのメソッドで関数を適用する場合、

- 要素（スカラー値）に対する関数
    - Seriesの各要素に適用：`map()`, `apply()`
    - DataFrameの各要素に適用：`applymap()`
- 行・列（一次元配列）に対する関数
    - DataFrameの各行・各列に適用：`apply()`

がある。