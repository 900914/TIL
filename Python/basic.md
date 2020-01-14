### 豆知識

- 関数とメソッドの違いはなにか？単独で呼び出せるのが関数（`len()`)、変数や値につけて呼び出すのがメソッド（`.join()`)
- メソッドはデータ型に紐付いた関数なので、呼び出せる関数はデータ型によって異なる。`.append()`は、リスト型の変数には使えるが辞書型には使えない。

### PYQ

- リストの要素確認
```python
zen = "Beautiful is better than ugly."
if 'Beautyful' in zen:
    print('"better" is included!')
``` 
- 変数に何かしら計算をして、結果を元の変数に代入する式、`x = x + 1 `を省略して `x += 1`とする方法を代入演算子（`=`以外の演算子は複合代入演算子という）


- `with open(...) as f`文。`with`文のブロックが終われば、自動的にファイルを閉じてくれる。`f = open(...)`の場合は`f.close()`を必要とするため忘れてしまう場合がある。

- 文字列の分割 `split()`
```python
sample = 'a,b,c,d,e'
sample_list = sample.split(',')
print(sample_list)

# ['a', 'b', 'c', 'd', 'e']
```
- 末尾の文字列削除 `rstrip()`

`rstrip()`メソッドは文字列を返し、`split()`メソッドはリストを返す。