
## pandas.DataFrame.interpolate

欠損値NaNを前後の値から補間する  

- 行 or 列を指定: 引数axis(デフォルトは列に対して行われる)
- 補間する連続欠損値の最大数を指定: 引数limit　
- 補間方向を指定: 引数limit_direction
- 内挿のみ or 外挿のみ or 両方を指定: 引数limit_area
- オブジェクト自体を更新するかを指定: 引数inplace
- 保管方法： 引数method(デフォルトはlinier)